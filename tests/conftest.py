import sys
from pathlib import Path

import pytest
from werkzeug.security import generate_password_hash

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import app as app_module
import database

TEST_USERNAME = "testadmin"
TEST_PASSWORD = "testpass123"


@pytest.fixture()
def client(tmp_path, monkeypatch):
    """A Flask test client wired to a throwaway SQLite file per test -- never touches the real
    helpdesk.db, and never depends on the real admin password."""
    monkeypatch.setattr(database, "DB_PATH", tmp_path / "test_helpdesk.db")
    monkeypatch.setattr(app_module.config, "ADMIN_USERNAME", TEST_USERNAME)
    monkeypatch.setattr(app_module.config, "ADMIN_PASSWORD_HASH", generate_password_hash(TEST_PASSWORD))

    database.init_db()
    app_module.app.config.update(TESTING=True)
    # Most tests post plain form data without a CSRF token -- CSRF enforcement itself is
    # covered separately and deliberately in tests/test_csrf.py with it left ON.
    monkeypatch.setitem(app_module.app.config, "WTF_CSRF_ENABLED", False)
    with app_module.app.test_client() as test_client:
        yield test_client


@pytest.fixture()
def logged_in_client(client):
    client.post("/login", data={"username": TEST_USERNAME, "password": TEST_PASSWORD})
    return client
