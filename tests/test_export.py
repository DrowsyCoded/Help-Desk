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


def test_csv_export_has_header_and_row(logged_in_client):
    submit(logged_in_client)
    resp = logged_in_client.get("/tickets/export.csv")
    assert resp.status_code == 200
    assert resp.headers["Content-Type"].startswith("text/csv")
    body = resp.data.decode()
    assert body.startswith("ID,Device,Submitted By,Issue,Status,Priority,Category")
    assert "Test PC" in body


def test_csv_export_respects_active_filters(logged_in_client):
    submit(logged_in_client, device_name="Urgent Device", priority="Urgent")
    submit(logged_in_client, device_name="Low Device", priority="Low")

    resp = logged_in_client.get("/tickets/export.csv?priority=Urgent")
    body = resp.data.decode()
    assert "Urgent Device" in body
    assert "Low Device" not in body
