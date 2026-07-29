import re

import app as app_module


def get_csrf_token(client, path):
    html = client.get(path).get_data(as_text=True)
    match = re.search(r'name="csrf_token" value="([^"]+)"', html)
    assert match, f"no csrf_token field found on {path}"
    return match.group(1)


def test_submit_without_csrf_token_is_rejected(client, monkeypatch):
    monkeypatch.setitem(app_module.app.config, "WTF_CSRF_ENABLED", True)
    resp = client.post("/submit", data={
        "device_name": "No Token PC", "submitted_by": "Jon", "issue_description": "x",
    })
    assert resp.status_code == 400


def test_submit_with_valid_csrf_token_succeeds(client, monkeypatch):
    monkeypatch.setitem(app_module.app.config, "WTF_CSRF_ENABLED", True)
    token = get_csrf_token(client, "/submit")
    resp = client.post("/submit", data={
        "device_name": "Token PC", "submitted_by": "Jon", "issue_description": "x",
        "csrf_token": token,
    }, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Ticket submitted" in resp.data


def test_login_without_csrf_token_is_rejected(client, monkeypatch):
    monkeypatch.setitem(app_module.app.config, "WTF_CSRF_ENABLED", True)
    resp = client.post("/login", data={"username": "testadmin", "password": "testpass123"})
    assert resp.status_code == 400


def test_api_post_stays_exempt_even_with_csrf_enabled(client, monkeypatch):
    """The JSON API must keep working with no token, even when CSRF is globally ON --
    scripts/tools calling it have no browser session to hold a token in."""
    monkeypatch.setitem(app_module.app.config, "WTF_CSRF_ENABLED", True)
    resp = client.post(
        "/api/tickets",
        json={"device_name": "API PC", "submitted_by": "Script", "issue_description": "x"},
    )
    assert resp.status_code == 201
