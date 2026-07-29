def submit(client, **overrides):
    data = {
        "device_name": "Test PC",
        "submitted_by": "Jonathon",
        "issue_description": "Won't boot",
        "priority": "High",
        "category": "Hardware",
    }
    data.update(overrides)
    return client.post("/submit", data=data, follow_redirects=True)


def test_empty_dashboard_does_not_crash(logged_in_client):
    resp = logged_in_client.get("/dashboard")
    assert resp.status_code == 200


def test_dashboard_renders_three_charts_with_data(logged_in_client):
    submit(logged_in_client, device_name="PC1", priority="High", category="Hardware")
    submit(logged_in_client, device_name="PC2", priority="Urgent", category="Network")

    resp = logged_in_client.get("/dashboard")
    body = resp.data.decode()
    assert body.count("<svg") == 3   # status chart, priority chart, volume chart
    assert "Urgent" in body
