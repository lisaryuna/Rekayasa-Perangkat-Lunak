def test_create_and_complete_action_item(client):
    payload = {"description": "Ship it"}
    r = client.post("/action-items/", json=payload)
    assert r.status_code == 201, r.text
    body = r.json()
    assert body["ok"] is True
    item = body["data"]
    assert item["completed"] is False

    r = client.put(f"/action-items/{item['id']}/complete")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    done = body["data"]
    assert done["completed"] is True

    r = client.get("/action-items/")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["data"]["total"] == 1
    assert len(body["data"]["items"]) == 1
    assert "total" in body["data"]
    assert len(body["data"]["items"]) == 1
    assert body["data"]["total"] == 1


def test_complete_action_item_not_found(client):
    r = client.put("/action-items/99999/complete")
    assert r.status_code == 404
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "NOT_FOUND"
    assert "message" in body["error"]


def test_create_action_item_validation_error_empty_description(client):
    r = client.post("/action-items/", json={"description": ""})
    assert r.status_code == 422
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "VALIDATION_ERROR"


def test_create_action_item_validation_error_missing_field(client):
    r = client.post("/action-items/", json={})
    assert r.status_code == 422
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "VALIDATION_ERROR"


def test_action_items_pagination_defaults(client):
    """Default page=1, page_size=10 returns items and total."""
    for i in range(3):
        client.post("/action-items/", json={"description": f"Task {i}"})

    r = client.get("/action-items/")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["data"]["total"] == 3
    assert len(body["data"]["items"]) == 3


def test_action_items_pagination_page_size(client):
    """page_size limits results; page selects the correct slice."""
    for i in range(5):
        client.post("/action-items/", json={"description": f"Task {i}"})

    r = client.get("/action-items/", params={"page": 1, "page_size": 2})
    assert r.status_code == 200
    body = r.json()
    assert body["data"]["total"] == 5
    assert len(body["data"]["items"]) == 2

    r = client.get("/action-items/", params={"page": 3, "page_size": 2})
    assert r.status_code == 200
    body = r.json()
    assert len(body["data"]["items"]) == 1  # last page has only 1 item


def test_action_items_empty_last_page(client):
    """Requesting a page beyond total rows returns empty items with correct total."""
    client.post("/action-items/", json={"description": "Only one"})

    r = client.get("/action-items/", params={"page": 99, "page_size": 10})
    assert r.status_code == 200
    body = r.json()
    assert body["data"]["total"] == 1
    assert body["data"]["items"] == []


def test_action_items_page_size_larger_than_total(client):
    """page_size larger than total still returns all items."""
    for i in range(3):
        client.post("/action-items/", json={"description": f"T{i}"})

    r = client.get("/action-items/", params={"page": 1, "page_size": 100})
    assert r.status_code == 200
    body = r.json()
    assert body["data"]["total"] == 3
    assert len(body["data"]["items"]) == 3
