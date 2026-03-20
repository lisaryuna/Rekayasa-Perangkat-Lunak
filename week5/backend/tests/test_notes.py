def test_create_and_list_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    body = r.json()
    assert body["ok"] is True
    data = body["data"]
    assert data["title"] == "Test"
    note_id = data["id"]

    r = client.get("/notes/")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["data"]["total"] >= 1
    assert len(body["data"]["items"]) >= 1
    assert "total" in body["data"]
    assert len(body["data"]["items"]) >= 1
    assert body["data"]["total"] >= 1

    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["data"]["id"] == note_id

    r = client.get("/notes/search/")
    assert r.status_code == 200
    assert r.json()["ok"] is True

    r = client.get("/notes/search/", params={"q": "Hello"})
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert len(body["data"]) >= 1


def test_get_note_not_found(client):
    r = client.get("/notes/99999")
    assert r.status_code == 404
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "NOT_FOUND"
    assert "message" in body["error"]


def test_create_note_validation_error_empty_title(client):
    r = client.post("/notes/", json={"title": "", "content": "Some content"})
    assert r.status_code == 422
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "VALIDATION_ERROR"


def test_create_note_validation_error_missing_field(client):
    r = client.post("/notes/", json={"title": "Only title"})
    assert r.status_code == 422
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "VALIDATION_ERROR"


def test_notes_pagination_defaults(client):
    """Default page=1, page_size=10 returns items and total."""
    for i in range(3):
        client.post("/notes/", json={"title": f"Note {i}", "content": "body"})

    r = client.get("/notes/")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["data"]["total"] == 3
    assert len(body["data"]["items"]) == 3


def test_notes_pagination_page_size(client):
    """page_size limits results; page selects the correct slice."""
    for i in range(5):
        client.post("/notes/", json={"title": f"Note {i}", "content": "body"})

    r = client.get("/notes/", params={"page": 1, "page_size": 2})
    assert r.status_code == 200
    body = r.json()
    assert body["data"]["total"] == 5
    assert len(body["data"]["items"]) == 2

    r = client.get("/notes/", params={"page": 3, "page_size": 2})
    assert r.status_code == 200
    body = r.json()
    assert len(body["data"]["items"]) == 1  # last page has only 1 item


def test_notes_empty_last_page(client):
    """Requesting a page beyond total rows returns empty items with correct total."""
    client.post("/notes/", json={"title": "Only", "content": "one"})

    r = client.get("/notes/", params={"page": 99, "page_size": 10})
    assert r.status_code == 200
    body = r.json()
    assert body["data"]["total"] == 1
    assert body["data"]["items"] == []


def test_notes_page_size_larger_than_total(client):
    """page_size larger than total still returns all items."""
    for i in range(3):
        client.post("/notes/", json={"title": f"N{i}", "content": "x"})

    r = client.get("/notes/", params={"page": 1, "page_size": 100})
    assert r.status_code == 200
    body = r.json()
    assert body["data"]["total"] == 3
    assert len(body["data"]["items"]) == 3
