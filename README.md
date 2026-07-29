# Help Desk Ticket Tracker

A small Flask + SQLite app to log and manage tech-support tickets for computers you help take care of
(your own machines, family/friends' devices, etc).

## Setup (first time)

```
cd helpdesk_tracker
pip install -r requirements.txt
```

## Run it

```
python app.py
```

This starts the server on your machine and prints a local address like `http://127.0.0.1:5000`.

## Letting other computers submit tickets to you

The app listens on `0.0.0.0`, meaning it's reachable from other devices on the same Wi-Fi/network, not
just this PC. To let another computer submit a ticket to you:

1. Find this machine's local network IP address:
   - Windows: open a terminal and run `ipconfig`, look for "IPv4 Address" under your active adapter
     (usually something like `192.168.1.XX`).
2. On the OTHER computer (must be on the same network), open a browser and go to:
   `http://<this-machine's-IP>:5000/submit`
3. They fill out the form (device name, their name, the issue) and it lands directly in your tracker.
4. You manage everything from THIS machine at `http://127.0.0.1:5000/tickets` (list/search) and
   `http://127.0.0.1:5000/dashboard` (stats).

If another computer can't reach it, check Windows Firewall isn't blocking inbound connections on port
5000 for Python -- it may prompt you to allow it the first time you run the app.

**Note:** this only works for devices on the same local network (home Wi-Fi/LAN). If you want tickets
submittable from anywhere on the internet (e.g. while you're away from home), that needs actually
deploying the app to a hosting service instead of running it locally -- ask if you want that set up.

## Messaging center

Each ticket now has a real two-way conversation, not just the automatic activity log:

- When someone submits a ticket, they get a **private link** (`/t/<token>`) shown on the confirmation
  page -- no login needed, the long random token is what identifies them. Bookmark it to check back.
- On that page they can see any replies from you and **send messages back**.
- On the admin ticket detail page (`/tickets/<id>`), you see the same conversation and can **reply** --
  your replies show up on their page labeled "Support," theirs show up on yours labeled by their name.
- The submitter's link is also shown on the admin ticket page if you need to resend it to them.
- Every message also drops a line in the ticket's activity log ("New message from submitter/admin"),
  so the full history stays in one place.

## Remote access requests

On a ticket's admin page, you can send a **Windows Quick Assist** request:

1. On your own PC, open Quick Assist -> "Give assistance" -> get a security code.
2. Paste that code into the "Send Remote Access Request" box on the ticket.
3. The submitter gets clear step-by-step instructions (plus the code) both as a message in the
   conversation and as a highlighted banner at the top of their ticket page telling them exactly
   how to open Quick Assist and enter it.
4. Once you're done helping, click "Mark Session Complete" on the ticket to close it out (this
   also logs it in the activity trail).

This coordinates the *handoff* -- actually connecting and controlling their screen still happens
in Quick Assist itself (built into Windows, free, no extra software needed on either end).

## JSON API

All endpoints are under `/api/`. Creating a ticket needs no auth (same as the web form, so scripts
can auto-file tickets); reading/updating tickets needs either an active admin login session
(browser) or an `X-API-Key` header (scripts/tools). The key lives in `config.py`.

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/tickets` | none | Create a ticket. Body: `device_name`, `submitted_by`, `issue_description` (required), `priority`, `category` (optional) |
| GET | `/api/tickets` | required | List tickets. Supports the same `?status=`, `?priority=`, `?category=`, `?q=` filters as the web UI |
| GET | `/api/tickets/<id>` | required | Get one ticket, including its full activity log |
| PATCH | `/api/tickets/<id>` | required | Partially update a ticket. Body: any of `status`, `priority`, `category`, `diagnosis_notes`, `fix_applied`, `time_spent_minutes` -- only the fields you send are changed |

Example (PowerShell):
```powershell
# File a ticket from a script -- no auth needed
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/tickets -Method Post -ContentType 'application/json' `
  -Body '{"device_name":"Backup Script","submitted_by":"Automation","issue_description":"Nightly backup failed","priority":"High"}'

# Read tickets using the API key instead of logging in
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/tickets -Headers @{ 'X-API-Key' = '<the key from config.py>' }
```

## Running tests

```
pip install -r requirements-dev.txt
pytest
```

Tests run against a throwaway SQLite database (never your real `helpdesk.db`) and a throwaway
admin login (never your real password), so they're always safe to run.

## Project structure

```
app.py              - routes and app logic
database.py         - SQLite schema and connection helper
templates/           - HTML pages (Jinja2)
static/style.css     - styling
helpdesk.db          - created automatically on first run (not committed to git if you set up a repo)
tests/                - pytest suite (auth, ticket CRUD, filters, CSV export)
```
