def test_create_list_and_patch_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"
    assert "created_at" in data and "updated_at" in data

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/", params={"q": "Hello", "limit": 10, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    note_id = data["id"]
    r = client.patch(f"/notes/{note_id}", json={"title": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["title"] == "Updated"


def test_notes_pagination_and_sorting(client):
    # Setup: Create 5 notes with distinct titles
    titles = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    notes = []
    for title in titles:
        payload = {"title": title, "content": f"Content for {title}"}
        r = client.post("/notes/", json=payload)
        assert r.status_code == 201, r.text
        data = r.json()
        notes.append(data)
    
    assert len(notes) == 5
    
    # Test pagination: limit=2 (default sort -created_at)
    r = client.get("/notes/?limit=2&sort=created_at")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 2
    assert items[0]["title"] == "Alpha"  # first created
    
    # Test pagination: skip=2 (3rd note first, default sort)
    r = client.get("/notes/?skip=2")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 3  # default limit=50
    assert items[0]["title"] == "Charlie"  # 3rd created
    
    # Test sorting asc title
    r = client.get("/notes/?sort=title")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 5
    item_titles = [item["title"] for item in items]
    assert item_titles == ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    
    # Test sorting desc title
    r = client.get("/notes/?sort=-title")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 5
    item_titles = [item["title"] for item in items]
    assert item_titles == ["Echo", "Delta", "Charlie", "Bravo", "Alpha"]
    
    # Combined: pagination + sorting
    r = client.get("/notes/?sort=title&skip=1&limit=2")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 2
    item_titles = [item["title"] for item in items]
    assert item_titles == ["Bravo", "Charlie"]
