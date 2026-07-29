def test_submit_page_is_public(client):
    resp = client.get("/submit")
    assert resp.status_code == 200


def test_protected_routes_redirect_when_not_logged_in(client):
    for path in ["/tickets", "/dashboard", "/tickets/export.csv"]:
        resp = client.get(path, follow_redirects=False)
        assert resp.status_code == 302
        assert "/login" in resp.headers["Location"]


def test_login_rejects_wrong_password(client):
    resp = client.post("/login", data={"username": "testadmin", "password": "wrong"})
    assert b"Wrong username or password" in resp.data


def test_login_rejects_wrong_username(client):
    resp = client.post("/login", data={"username": "nobody", "password": "testpass123"})
    assert b"Wrong username or password" in resp.data


def test_login_succeeds_with_correct_credentials(logged_in_client):
    resp = logged_in_client.get("/tickets")
    assert resp.status_code == 200


def test_logout_clears_session(logged_in_client):
    logged_in_client.get("/logout")
    resp = logged_in_client.get("/tickets", follow_redirects=False)
    assert resp.status_code == 302
