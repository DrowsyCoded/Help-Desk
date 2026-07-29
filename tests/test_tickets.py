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


def test_submit_creates_ticket_with_chosen_priority_and_category(logged_in_client):
    submit(logged_in_client)
    resp = logged_in_client.get("/tickets")
    assert b"Test PC" in resp.data
    assert b"High" in resp.data
    assert b"Hardware" in resp.data


def test_submit_without_priority_defaults_to_medium(logged_in_client):
    data = {
        "device_name": "Default PC",
        "submitted_by": "Jonathon",
        "issue_description": "Slow",
    }
    logged_in_client.post("/submit", data=data, follow_redirects=True)
    resp = logged_in_client.get("/tickets/1")
    assert b"Medium" in resp.data
    assert b"Other" in resp.data   # default category


def test_new_ticket_logs_a_creation_activity_entry(logged_in_client):
    submit(logged_in_client)
    resp = logged_in_client.get("/tickets/1")
    assert b"Ticket created" in resp.data


def test_search_filters_by_device_name(logged_in_client):
    submit(logged_in_client, device_name="Living Room PC")
    submit(logged_in_client, device_name="Kitchen Laptop")
    resp = logged_in_client.get("/tickets?q=Kitchen")
    assert b"Kitchen Laptop" in resp.data
    assert b"Living Room PC" not in resp.data


def test_filters_by_priority_and_category(logged_in_client):
    submit(logged_in_client, device_name="Urgent Device", priority="Urgent", category="Network")
    submit(logged_in_client, device_name="Low Device", priority="Low", category="Software")

    resp = logged_in_client.get("/tickets?priority=Urgent")
    assert b"Urgent Device" in resp.data
    assert b"Low Device" not in resp.data

    resp = logged_in_client.get("/tickets?category=Software")
    assert b"Low Device" in resp.data
    assert b"Urgent Device" not in resp.data


def test_update_ticket_logs_correctly_cased_activity_message(logged_in_client):
    """Regression test: an earlier bug used str.capitalize() on the activity message, which
    silently lowercased proper-cased values like 'Open' and 'In Progress' into 'open' and
    'in progress'. This must never happen again."""
    submit(logged_in_client)
    resp = logged_in_client.post(
        "/tickets/1",
        data={
            "status": "In Progress",
            "priority": "Urgent",
            "category": "Hardware",
            "diagnosis_notes": "Bad PSU",
            "fix_applied": "",
            "time_spent_minutes": "20",
        },
        follow_redirects=True,
    )
    assert b"Status changed from Open to In Progress" in resp.data
    assert b"priority changed from High to Urgent" in resp.data
    assert b"status changed from open to in progress" not in resp.data   # the old, broken casing


def test_resolving_ticket_sets_date_resolved(logged_in_client):
    submit(logged_in_client)
    resp = logged_in_client.post(
        "/tickets/1",
        data={
            "status": "Resolved",
            "priority": "High",
            "category": "Hardware",
            "diagnosis_notes": "Bad PSU",
            "fix_applied": "Replaced PSU",
            "time_spent_minutes": "45",
        },
        follow_redirects=True,
    )
    assert b"Resolved on" in resp.data


def test_resolving_twice_does_not_overwrite_original_resolved_date(logged_in_client):
    submit(logged_in_client)
    resolve_data = {
        "status": "Resolved", "priority": "High", "category": "Hardware",
        "diagnosis_notes": "Bad PSU", "fix_applied": "Replaced PSU", "time_spent_minutes": "45",
    }
    first = logged_in_client.post("/tickets/1", data=resolve_data, follow_redirects=True)
    second = logged_in_client.post("/tickets/1", data=resolve_data, follow_redirects=True)

    def extract_resolved_line(html):
        idx = html.find(b"Resolved on")
        return html[idx:idx + 40]

    assert extract_resolved_line(first.data) == extract_resolved_line(second.data)
