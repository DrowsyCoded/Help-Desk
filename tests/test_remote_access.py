import re


def extract_token(html):
    match = re.search(r'/t/([A-Za-z0-9_-]+)', html)
    assert match
    return match.group(1)


def submit_and_get_token(client):
    resp = client.post("/submit", data={
        "device_name": "Test PC", "submitted_by": "Jonathon", "issue_description": "Won't boot",
    }, follow_redirects=True)
    return extract_token(resp.data.decode())


def test_sending_remote_access_request_stores_code_and_notifies_submitter(logged_in_client):
    token = submit_and_get_token(logged_in_client)
    resp = logged_in_client.post(
        "/tickets/1/remote-access", data={"quick_assist_code": "123 456"}, follow_redirects=True
    )
    assert resp.status_code == 200
    assert b"123 456" in resp.data   # visible on the admin page

    submitter_resp = logged_in_client.get(f"/t/{token}")
    assert b"Remote help is available" in submitter_resp.data
    assert b"123 456" in submitter_resp.data
    assert b"Quick Assist" in submitter_resp.data


def test_remote_access_request_appears_in_conversation_and_activity_log(logged_in_client):
    submit_and_get_token(logged_in_client)
    logged_in_client.post("/tickets/1/remote-access", data={"quick_assist_code": "999999"}, follow_redirects=True)

    resp = logged_in_client.get("/tickets/1")
    assert b"999999" in resp.data
    assert b"New message from admin" in resp.data


def test_marking_remote_session_complete_updates_status_and_logs_it(logged_in_client):
    token = submit_and_get_token(logged_in_client)
    logged_in_client.post("/tickets/1/remote-access", data={"quick_assist_code": "123456"}, follow_redirects=True)

    resp = logged_in_client.post("/tickets/1/remote-complete", follow_redirects=True)
    assert b"Remote access session marked complete" in resp.data
    assert b"Last session completed" in resp.data

    # the banner should no longer show on the submitter's page once completed
    submitter_resp = logged_in_client.get(f"/t/{token}")
    assert b"Remote help is available" not in submitter_resp.data


def test_blank_code_does_not_create_a_pending_request(logged_in_client):
    submit_and_get_token(logged_in_client)
    logged_in_client.post("/tickets/1/remote-access", data={"quick_assist_code": "  "}, follow_redirects=True)
    resp = logged_in_client.get("/tickets/1")
    assert b"waiting on them to connect" not in resp.data


def test_remote_access_routes_require_login(client):
    submit_and_get_token(client)
    resp = client.post("/tickets/1/remote-access", data={"quick_assist_code": "123456"}, follow_redirects=False)
    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]

    resp = client.post("/tickets/1/remote-complete", follow_redirects=False)
    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]
