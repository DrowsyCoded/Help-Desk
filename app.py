import csv
import io
import secrets
from datetime import datetime, timedelta

try:
    from flask import Flask, jsonify, redirect, render_template, request, session, url_for
    from flask_wtf import CSRFProtect
except ModuleNotFoundError:
    print("ERROR: Flask (or Flask-WTF) isn't installed for this Python.")
    print("Fix: run   python -m pip install -r requirements.txt")
    input("\nPress Enter to close...")
    raise SystemExit(1)

from functools import wraps

from werkzeug.security import check_password_hash

from database import get_db, init_db
import config
from charts import bar_chart_svg, line_chart_svg

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
csrf = CSRFProtect(app)

STATUSES = ["Open", "In Progress", "Resolved"]
PRIORITIES = ["Low", "Medium", "High", "Urgent"]
CATEGORIES = ["Hardware", "Software", "Network", "Other"]

STATUS_COLORS = {"Open": "#f0a85e", "In Progress": "#5e9ff0", "Resolved": "#5ed88a"}
PRIORITY_COLORS = {"Low": "#8a8a9a", "Medium": "#c7c7d6", "High": "#f0a85e", "Urgent": "#ff6b6b"}


def log_activity(db, ticket_id, message):
    db.execute(
        "INSERT INTO ticket_activity (ticket_id, timestamp, message) VALUES (?, ?, ?)",
        (ticket_id, datetime.now().isoformat(timespec="seconds"), message),
    )


def create_ticket(db, device_name, submitted_by, issue_description, priority="Medium", category="Other"):
    """Shared by the web form and the JSON API so both paths behave identically.
    Returns (ticket_id, access_token) -- the token is a private, unguessable link the submitter
    uses to view/reply to their ticket later without needing a login."""
    token = secrets.token_urlsafe(16)
    cur = db.execute(
        """INSERT INTO tickets
           (device_name, submitted_by, issue_description, status, date_submitted, priority, category, access_token)
           VALUES (?, ?, ?, 'Open', ?, ?, ?, ?)""",
        (device_name, submitted_by, issue_description, datetime.now().isoformat(timespec="seconds"),
         priority, category, token),
    )
    log_activity(db, cur.lastrowid, "Ticket created")
    db.commit()
    return cur.lastrowid, token


def apply_ticket_update(db, ticket_id, changes):
    """Shared by the web ticket-detail form and the JSON API's PATCH endpoint.
    `changes` may contain any of: status, priority, category, diagnosis_notes, fix_applied,
    time_spent_minutes. Only keys present are changed (true partial update) -- keys omitted
    entirely keep their existing value. Returns the updated row, or None if no such ticket.
    """
    existing = db.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    if existing is None:
        return None

    new_status = changes.get("status", existing["status"])
    new_priority = changes.get("priority", existing["priority"])
    new_category = changes.get("category", existing["category"])
    new_diagnosis = changes.get("diagnosis_notes", existing["diagnosis_notes"])
    new_fix = changes.get("fix_applied", existing["fix_applied"])
    new_time_spent = changes.get("time_spent_minutes", existing["time_spent_minutes"])

    date_resolved = existing["date_resolved"]
    if new_status == "Resolved" and existing["date_resolved"] is None:
        date_resolved = datetime.now().isoformat(timespec="seconds")

    db.execute(
        """UPDATE tickets SET status = ?, priority = ?, category = ?, diagnosis_notes = ?,
           fix_applied = ?, time_spent_minutes = ?, date_resolved = ? WHERE id = ?""",
        (new_status, new_priority, new_category, new_diagnosis, new_fix, new_time_spent, date_resolved, ticket_id),
    )

    changed = []
    if new_status != existing["status"]:
        changed.append(f"status changed from {existing['status']} to {new_status}")
    if new_priority != existing["priority"]:
        changed.append(f"priority changed from {existing['priority']} to {new_priority}")
    if new_category != existing["category"]:
        changed.append(f"category changed from {existing['category']} to {new_category}")
    if new_diagnosis and new_diagnosis != (existing["diagnosis_notes"] or ""):
        changed.append("diagnosis notes updated")
    if new_fix and new_fix != (existing["fix_applied"] or ""):
        changed.append("fix applied updated")
    if changed:
        message = "; ".join(changed)
        message = message[0].upper() + message[1:]   # capitalize only the first letter, not the whole string
        log_activity(db, ticket_id, message)

    db.commit()
    return db.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()


def ticket_to_dict(row):
    return {
        "id": row["id"], "device_name": row["device_name"], "submitted_by": row["submitted_by"],
        "issue_description": row["issue_description"], "status": row["status"], "priority": row["priority"],
        "category": row["category"], "date_submitted": row["date_submitted"],
        "diagnosis_notes": row["diagnosis_notes"], "fix_applied": row["fix_applied"],
        "time_spent_minutes": row["time_spent_minutes"], "date_resolved": row["date_resolved"],
        "access_token": row["access_token"],
    }


def quick_assist_instructions(code):
    return (
        "I'd like to help with this remotely using Windows Quick Assist (built into Windows, free):\n\n"
        "1. Press the Windows key, type \"Quick Assist\", and open it.\n"
        "2. Click \"Get help\".\n"
        f"3. Enter this security code when asked: {code}\n"
        "4. When I connect, click \"Allow\" to let me see (and if needed, control) your screen.\n\n"
        "Reply here once you're connected or if you run into any trouble."
    )


def post_message(db, ticket_id, sender, body):
    db.execute(
        "INSERT INTO ticket_messages (ticket_id, sender, body, timestamp) VALUES (?, ?, ?, ?)",
        (ticket_id, sender, body, datetime.now().isoformat(timespec="seconds")),
    )
    who = "admin" if sender == "admin" else "submitter"
    log_activity(db, ticket_id, f"New message from {who}")
    db.commit()


def api_authenticated():
    """Accepts either an active admin login session (browser) or an X-API-Key header (scripts)."""
    if session.get("logged_in"):
        return True
    api_key = request.headers.get("X-API-Key", "")
    return bool(api_key) and api_key == config.API_KEY


def api_login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not api_authenticated():
            return jsonify({"error": "Unauthorized"}), 401
        return view(*args, **kwargs)
    return wrapped


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)
    return wrapped


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == config.ADMIN_USERNAME and check_password_hash(config.ADMIN_PASSWORD_HASH, password):
            session["logged_in"] = True
            session["username"] = username
            next_url = request.args.get("next") or url_for("list_tickets")
            return redirect(next_url)
        error = "Wrong username or password."
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
def index():
    return redirect(url_for("list_tickets"))


@app.route("/submit", methods=["GET", "POST"])
def submit_ticket():
    if request.method == "POST":
        db = get_db()
        _ticket_id, token = create_ticket(
            db,
            request.form["device_name"].strip(),
            request.form["submitted_by"].strip(),
            request.form["issue_description"].strip(),
            request.form.get("priority", "Medium"),
            request.form.get("category", "Other"),
        )
        db.close()
        return redirect(url_for("submitted", token=token))
    return render_template("submit.html", priorities=PRIORITIES, categories=CATEGORIES)


@app.route("/submitted")
def submitted():
    return render_template("submitted.html", token=request.args.get("token"))


@app.route("/t/<token>", methods=["GET", "POST"])
def my_ticket(token):
    """Public, no-login page a ticket submitter uses to check status and message back --
    identified purely by the private token, not an account."""
    db = get_db()
    ticket = db.execute("SELECT * FROM tickets WHERE access_token = ?", (token,)).fetchone()
    if ticket is None:
        db.close()
        return render_template("my_ticket_not_found.html"), 404

    if request.method == "POST":
        body = request.form.get("message", "").strip()
        if body:
            post_message(db, ticket["id"], "submitter", body)
        db.close()
        return redirect(url_for("my_ticket", token=token))

    messages = db.execute(
        "SELECT * FROM ticket_messages WHERE ticket_id = ? ORDER BY timestamp ASC", (ticket["id"],)
    ).fetchall()
    db.close()
    return render_template("my_ticket.html", ticket=ticket, messages=messages)


def build_ticket_query():
    """Shared filter logic for the ticket list view and the CSV export, so they never drift apart."""
    status_filter = request.args.get("status", "")
    priority_filter = request.args.get("priority", "")
    category_filter = request.args.get("category", "")
    search = request.args.get("q", "").strip()

    query = "SELECT * FROM tickets WHERE 1=1"
    params = []
    if status_filter:
        query += " AND status = ?"
        params.append(status_filter)
    if priority_filter:
        query += " AND priority = ?"
        params.append(priority_filter)
    if category_filter:
        query += " AND category = ?"
        params.append(category_filter)
    if search:
        query += " AND (device_name LIKE ? OR submitted_by LIKE ? OR issue_description LIKE ?)"
        like = f"%{search}%"
        params.extend([like, like, like])
    query += " ORDER BY date_submitted DESC"
    return query, params, status_filter, priority_filter, category_filter, search


@app.route("/tickets")
@login_required
def list_tickets():
    query, params, status_filter, priority_filter, category_filter, search = build_ticket_query()

    db = get_db()
    tickets = db.execute(query, params).fetchall()
    db.close()
    return render_template(
        "tickets.html",
        tickets=tickets,
        statuses=STATUSES,
        priorities=PRIORITIES,
        categories=CATEGORIES,
        status_filter=status_filter,
        priority_filter=priority_filter,
        category_filter=category_filter,
        search=search,
    )


@app.route("/tickets/export.csv")
@login_required
def export_csv():
    query, params, *_ = build_ticket_query()
    db = get_db()
    tickets = db.execute(query, params).fetchall()
    db.close()

    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "ID", "Device", "Submitted By", "Issue", "Status", "Priority", "Category",
        "Date Submitted", "Diagnosis Notes", "Fix Applied", "Time Spent (min)", "Date Resolved",
    ])
    for t in tickets:
        writer.writerow([
            t["id"], t["device_name"], t["submitted_by"], t["issue_description"], t["status"],
            t["priority"], t["category"], t["date_submitted"], t["diagnosis_notes"], t["fix_applied"],
            t["time_spent_minutes"], t["date_resolved"],
        ])

    return app.response_class(
        buffer.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=tickets_export.csv"},
    )


@app.route("/tickets/<int:ticket_id>", methods=["GET", "POST"])
@login_required
def ticket_detail(ticket_id):
    db = get_db()
    if request.method == "POST":
        time_spent = request.form.get("time_spent_minutes", "").strip()
        time_spent_val = int(time_spent) if time_spent.isdigit() else None
        apply_ticket_update(db, ticket_id, {
            "status": request.form["status"],
            "priority": request.form.get("priority", "Medium"),
            "category": request.form.get("category", "Other"),
            "diagnosis_notes": request.form.get("diagnosis_notes", "").strip(),
            "fix_applied": request.form.get("fix_applied", "").strip(),
            "time_spent_minutes": time_spent_val,
        })

    ticket = db.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    messages = db.execute(
        "SELECT * FROM ticket_messages WHERE ticket_id = ? ORDER BY timestamp ASC", (ticket_id,)
    ).fetchall()
    activity = db.execute(
        "SELECT * FROM ticket_activity WHERE ticket_id = ? ORDER BY timestamp DESC", (ticket_id,)
    ).fetchall()
    db.close()
    return render_template(
        "ticket_detail.html", ticket=ticket, statuses=STATUSES, priorities=PRIORITIES,
        categories=CATEGORIES, activity=activity, messages=messages,
    )


@app.route("/tickets/<int:ticket_id>/messages", methods=["POST"])
@login_required
def ticket_reply(ticket_id):
    db = get_db()
    body = request.form.get("message", "").strip()
    if body:
        post_message(db, ticket_id, "admin", body)
    db.close()
    return redirect(url_for("ticket_detail", ticket_id=ticket_id))


@app.route("/tickets/<int:ticket_id>/remote-access", methods=["POST"])
@login_required
def request_remote_access(ticket_id):
    """You generate this code yourself from your own Quick Assist app (Give assistance ->
    Get a security code) and paste it here -- this just sends it to the submitter with
    instructions and tracks that a session is pending."""
    db = get_db()
    code = request.form.get("quick_assist_code", "").strip()
    if code:
        db.execute(
            "UPDATE tickets SET remote_status = 'Requested', remote_code = ? WHERE id = ?", (code, ticket_id)
        )
        post_message(db, ticket_id, "admin", quick_assist_instructions(code))
        db.commit()
    db.close()
    return redirect(url_for("ticket_detail", ticket_id=ticket_id))


@app.route("/tickets/<int:ticket_id>/remote-complete", methods=["POST"])
@login_required
def complete_remote_access(ticket_id):
    db = get_db()
    db.execute("UPDATE tickets SET remote_status = 'Completed' WHERE id = ?", (ticket_id,))
    log_activity(db, ticket_id, "Remote access session marked complete")
    db.commit()
    db.close()
    return redirect(url_for("ticket_detail", ticket_id=ticket_id))


@app.route("/api/tickets", methods=["GET", "POST"])
@csrf.exempt   # this is a JSON API for scripts/tools, not a browser form -- they can't hold a CSRF token
def api_tickets():
    """POST is public (same as the /submit form) so scripts/other tools can auto-file tickets.
    GET requires auth (session login or X-API-Key header) since it exposes ticket data."""
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        required = ["device_name", "submitted_by", "issue_description"]
        missing = [f for f in required if not str(data.get(f, "")).strip()]
        if missing:
            return jsonify({"error": f"Missing required field(s): {', '.join(missing)}"}), 400

        priority = data.get("priority", "Medium")
        category = data.get("category", "Other")
        if priority not in PRIORITIES:
            return jsonify({"error": f"Invalid priority. Must be one of {PRIORITIES}"}), 400
        if category not in CATEGORIES:
            return jsonify({"error": f"Invalid category. Must be one of {CATEGORIES}"}), 400

        db = get_db()
        ticket_id, _token = create_ticket(
            db, str(data["device_name"]).strip(), str(data["submitted_by"]).strip(),
            str(data["issue_description"]).strip(), priority, category,
        )
        ticket = db.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
        db.close()
        return jsonify(ticket_to_dict(ticket)), 201

    if not api_authenticated():
        return jsonify({"error": "Unauthorized"}), 401
    query, params, *_ = build_ticket_query()
    db = get_db()
    tickets = db.execute(query, params).fetchall()
    db.close()
    return jsonify([ticket_to_dict(t) for t in tickets])


@app.route("/api/tickets/<int:ticket_id>", methods=["GET", "PATCH"])
@csrf.exempt
@api_login_required
def api_ticket_detail(ticket_id):
    db = get_db()

    if request.method == "PATCH":
        data = request.get_json(silent=True) or {}
        allowed_fields = {"status", "priority", "category", "diagnosis_notes", "fix_applied", "time_spent_minutes"}
        changes = {k: v for k, v in data.items() if k in allowed_fields}

        if "status" in changes and changes["status"] not in STATUSES:
            db.close()
            return jsonify({"error": f"Invalid status. Must be one of {STATUSES}"}), 400
        if "priority" in changes and changes["priority"] not in PRIORITIES:
            db.close()
            return jsonify({"error": f"Invalid priority. Must be one of {PRIORITIES}"}), 400
        if "category" in changes and changes["category"] not in CATEGORIES:
            db.close()
            return jsonify({"error": f"Invalid category. Must be one of {CATEGORIES}"}), 400

        updated = apply_ticket_update(db, ticket_id, changes)
        db.close()
        if updated is None:
            return jsonify({"error": "Ticket not found"}), 404
        return jsonify(ticket_to_dict(updated))

    ticket = db.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    if ticket is None:
        db.close()
        return jsonify({"error": "Ticket not found"}), 404
    activity_rows = db.execute(
        "SELECT timestamp, message FROM ticket_activity WHERE ticket_id = ? ORDER BY timestamp DESC", (ticket_id,)
    ).fetchall()
    db.close()
    result = ticket_to_dict(ticket)
    result["activity"] = [dict(a) for a in activity_rows]
    return jsonify(result)


@app.route("/dashboard")
@login_required
def dashboard():
    db = get_db()
    total = db.execute("SELECT COUNT(*) c FROM tickets").fetchone()["c"]
    by_status = db.execute("SELECT status, COUNT(*) c FROM tickets GROUP BY status").fetchall()
    resolved_times = db.execute(
        """SELECT time_spent_minutes FROM tickets
           WHERE status = 'Resolved' AND time_spent_minutes IS NOT NULL"""
    ).fetchall()
    top_devices = db.execute(
        "SELECT device_name, COUNT(*) c FROM tickets GROUP BY device_name ORDER BY c DESC LIMIT 5"
    ).fetchall()
    by_priority = db.execute("SELECT priority, COUNT(*) c FROM tickets GROUP BY priority").fetchall()
    volume_rows = db.execute(
        "SELECT substr(date_submitted, 1, 10) AS day, COUNT(*) c FROM tickets GROUP BY day"
    ).fetchall()
    db.close()

    avg_minutes = None
    if resolved_times:
        avg_minutes = round(sum(r["time_spent_minutes"] for r in resolved_times) / len(resolved_times), 1)

    status_chart = bar_chart_svg([
        (row["status"], row["c"], STATUS_COLORS.get(row["status"], "#6c6cf0")) for row in by_status
    ])
    priority_order = {p: i for i, p in enumerate(PRIORITIES)}
    priority_rows_sorted = sorted(by_priority, key=lambda row: priority_order.get(row["priority"], 99))
    priority_chart = bar_chart_svg([
        (row["priority"], row["c"], PRIORITY_COLORS.get(row["priority"], "#6c6cf0"))
        for row in priority_rows_sorted
    ])

    volume_map = {row["day"]: row["c"] for row in volume_rows}
    last_14_days = [(datetime.now() - timedelta(days=i)).date() for i in range(13, -1, -1)]
    volume_points = [(d.strftime("%m/%d"), volume_map.get(d.isoformat(), 0)) for d in last_14_days]
    volume_chart = line_chart_svg(volume_points)

    return render_template(
        "dashboard.html", total=total, by_status=by_status, avg_minutes=avg_minutes, top_devices=top_devices,
        status_chart=status_chart, priority_chart=priority_chart, volume_chart=volume_chart,
    )


if __name__ == "__main__":
    try:
        init_db()
        print("Starting Help Desk Tracker...")
        print("On this PC:      http://127.0.0.1:5000/tickets")
        print("From other PCs:  http://<this-PC's-LAN-IP>:5000/submit  (run ipconfig to find the IP)")
        print("Press Ctrl+C to stop.\n")
        # host=0.0.0.0 makes this reachable from other devices on the same network,
        # not just this machine -- that's what lets other computers submit tickets.
        app.run(host="0.0.0.0", port=5000, debug=False)
    except Exception:
        import traceback
        traceback.print_exc()
        input("\nSomething went wrong (see error above). Press Enter to close...")
