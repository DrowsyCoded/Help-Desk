import json

from tests.conftest import TEST_USERNAME, TEST_PASSWORD

TEST_API_KEY = "test-api-key-123"


def post_json(client, url, payload, headers=None):
    return client.post(url, data=json.dumps(payload), content_type="application/json", headers=headers or {})


def patch_json(client, url, payload, headers=None):
    return client.patch(url, data=json.dumps(payload), content_type="application/json", headers=headers or {})


def test_create_ticket_via_api_requires_no_auth(client):
    resp = post_json(client, "/api/tickets", {
        "device_name": "API PC", "submitted_by": "Script", "issue_description": "Auto-filed",
    })
    assert resp.status_code == 201
    body = resp.get_json()
    assert body["device_name"] == "API PC"
    assert body["status"] == "Open"
    assert body["priority"] == "Medium"   # default
    assert body["category"] == "Other"    # default


def test_create_ticket_via_api_rejects_missing_fields(client):
    resp = post_json(client, "/api/tickets", {"device_name": "API PC"})
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_create_ticket_via_api_rejects_invalid_priority(client):
    resp = post_json(client, "/api/tickets", {
        "device_name": "API PC", "submitted_by": "Script", "issue_description": "x", "priority": "Extreme",
    })
    assert resp.status_code == 400


def test_list_tickets_via_api_requires_auth(client):
    resp = client.get("/api/tickets")
    assert resp.status_code == 401


def test_list_tickets_via_api_with_session_login(logged_in_client):
    post_json(logged_in_client, "/api/tickets", {
        "device_name": "Session PC", "submitted_by": "Jon", "issue_description": "x",
    })
    resp = logged_in_client.get("/api/tickets")
    assert resp.status_code == 200
    devices = [t["device_name"] for t in resp.get_json()]
    assert "Session PC" in devices


def test_list_tickets_via_api_with_api_key(client, monkeypatch):
    import app as app_module
    monkeypatch.setattr(app_module.config, "API_KEY", TEST_API_KEY)

    post_json(client, "/api/tickets", {"device_name": "Key PC", "submitted_by": "Jon", "issue_description": "x"})
    resp = client.get("/api/tickets", headers={"X-API-Key": TEST_API_KEY})
    assert resp.status_code == 200

    resp_bad_key = client.get("/api/tickets", headers={"X-API-Key": "wrong-key"})
    assert resp_bad_key.status_code == 401


def test_get_single_ticket_via_api_includes_activity_log(logged_in_client):
    create = post_json(logged_in_client, "/api/tickets", {
        "device_name": "Detail PC", "submitted_by": "Jon", "issue_description": "x",
    })
    ticket_id = create.get_json()["id"]

    resp = logged_in_client.get(f"/api/tickets/{ticket_id}")
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["device_name"] == "Detail PC"
    assert any(a["message"] == "Ticket created" for a in body["activity"])


def test_get_nonexistent_ticket_via_api_returns_404(logged_in_client):
    resp = logged_in_client.get("/api/tickets/9999")
    assert resp.status_code == 404


def test_patch_ticket_via_api_updates_and_logs_activity(logged_in_client):
    create = post_json(logged_in_client, "/api/tickets", {
        "device_name": "Patch PC", "submitted_by": "Jon", "issue_description": "x", "priority": "Low",
    })
    ticket_id = create.get_json()["id"]

    resp = patch_json(logged_in_client, f"/api/tickets/{ticket_id}", {"status": "Resolved", "priority": "High"})
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["status"] == "Resolved"
    assert body["priority"] == "High"
    assert body["date_resolved"] is not None

    detail = logged_in_client.get(f"/api/tickets/{ticket_id}").get_json()
    messages = [a["message"] for a in detail["activity"]]
    assert any("Status changed from Open to Resolved" in m for m in messages)


def test_patch_ticket_via_api_is_a_true_partial_update(logged_in_client):
    """Fields not included in the PATCH body must be left untouched."""
    create = post_json(logged_in_client, "/api/tickets", {
        "device_name": "Partial PC", "submitted_by": "Jon", "issue_description": "x",
        "priority": "Urgent", "category": "Network",
    })
    ticket_id = create.get_json()["id"]

    resp = patch_json(logged_in_client, f"/api/tickets/{ticket_id}", {"status": "In Progress"})
    body = resp.get_json()
    assert body["status"] == "In Progress"
    assert body["priority"] == "Urgent"    # untouched
    assert body["category"] == "Network"   # untouched


def test_patch_ticket_via_api_rejects_invalid_status(logged_in_client):
    create = post_json(logged_in_client, "/api/tickets", {
        "device_name": "Bad Status PC", "submitted_by": "Jon", "issue_description": "x",
    })
    ticket_id = create.get_json()["id"]
    resp = patch_json(logged_in_client, f"/api/tickets/{ticket_id}", {"status": "Not A Real Status"})
    assert resp.status_code == 400


def test_patch_nonexistent_ticket_via_api_returns_404(logged_in_client):
    resp = patch_json(logged_in_client, "/api/tickets/9999", {"status": "Resolved"})
    assert resp.status_code == 404
