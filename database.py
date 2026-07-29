import secrets
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "helpdesk.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name TEXT NOT NULL,
    submitted_by TEXT NOT NULL,
    issue_description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Open',
    date_submitted TEXT NOT NULL,
    diagnosis_notes TEXT DEFAULT '',
    fix_applied TEXT DEFAULT '',
    time_spent_minutes INTEGER,
    date_resolved TEXT
);

CREATE TABLE IF NOT EXISTS ticket_activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
    message TEXT NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE TABLE IF NOT EXISTS ticket_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER NOT NULL,
    sender TEXT NOT NULL CHECK (sender IN ('admin', 'submitter')),
    body TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);
"""


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _migrate(conn):
    """Additive, non-destructive migrations for columns added after the initial schema."""
    existing_cols = {row[1] for row in conn.execute("PRAGMA table_info(tickets)")}
    if "priority" not in existing_cols:
        conn.execute("ALTER TABLE tickets ADD COLUMN priority TEXT NOT NULL DEFAULT 'Medium'")
    if "category" not in existing_cols:
        conn.execute("ALTER TABLE tickets ADD COLUMN category TEXT NOT NULL DEFAULT 'Other'")
    if "remote_status" not in existing_cols:
        conn.execute("ALTER TABLE tickets ADD COLUMN remote_status TEXT")
    if "remote_code" not in existing_cols:
        conn.execute("ALTER TABLE tickets ADD COLUMN remote_code TEXT")
    if "access_token" not in existing_cols:
        conn.execute("ALTER TABLE tickets ADD COLUMN access_token TEXT")
        # backfill tokens for any tickets that existed before this column did
        for row in conn.execute("SELECT id FROM tickets WHERE access_token IS NULL"):
            conn.execute(
                "UPDATE tickets SET access_token = ? WHERE id = ?", (secrets.token_urlsafe(16), row["id"])
            )


def init_db():
    conn = get_db()
    conn.executescript(SCHEMA)
    _migrate(conn)
    conn.commit()
    conn.close()
