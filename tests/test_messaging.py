import re


def extract_token_link(html):
    match = re.search(r'/t/([A-Za-z0-9_-]+)', html)
    assert match, "no submitter link found on the confirmation page"
    return match.group(1)


def submit_and_get_token(client, **overrides):
    data = {
        "device_name": "Test PC", "submitted_by": "Jonathon", "issue_description": "Won't boot",
        "priority": "High", "category": "Hardware",
    }
    data.update(overrides)
    resp = client.post("/submit", data=data, follow_redirects=True)
    return extract_token_link(resp.data.decode())


def test_submitting_a_ticket_shows_a_private_link(client):
    resp = client.post("/submit", data={
        "device_name": "Test PC", "submitted_by": "Jonathon", "issue_description": "Won't boot",
    }, follow_redirects=True)
    assert b"/t/" in resp.data


def test_submitter_can_view_their_ticket_via_token(client):
    token = submit_and_get_token(client)
    resp = client.get(f"/t/{token}")
    assert resp.status_code == 200
    assert b"Test PC" in resp.data


def test_invalid_token_returns_404(client):
    resp = client.get("/t/not-a-real-token")
    assert resp.status_code == 404


def test_submitter_can_post_a_message_and_it_shows_up_for_admin(client):
    token = submit_and_get_token(client)
    client.post(f"/t/{token}", data={"message": "Any update on this?"}, follow_redirects=True)

    resp = client.post("/login", data={"username": "testadmin", "password": "testpass123"}, follow_redirects=True)
    resp = client.get("/tickets/1")
    assert b"Any update on this?" in resp.data
    assert b"New message from submitter" in resp.data   # shows in the activity log too


def test_admin_can_reply_and_it_shows_up_for_submitter(logged_in_client):
    token = submit_and_get_token(logged_in_client)
    logged_in_client.post("/tickets/1/messages", data={"message": "Looking into it now."}, follow_redirects=True)

    resp = logged_in_client.get(f"/t/{token}")
    assert b"Looking into it now." in resp.data
    assert b"Support" in resp.data   # labeled as coming from support, not the submitter's own name


def test_empty_message_is_not_posted(client):
    token = submit_and_get_token(client)
    client.post(f"/t/{token}", data={"message": "   "}, follow_redirects=True)
    resp = client.get(f"/t/{token}")
    assert b"No messages yet." in resp.data


def test_admin_reply_route_requires_login(client):
    token = submit_and_get_token(client)
    resp = client.post("/tickets/1/messages", data={"message": "sneaky"}, follow_redirects=False)
    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]
