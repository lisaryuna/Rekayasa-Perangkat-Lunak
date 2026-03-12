def test_create_and_list_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/search/")
    assert r.status_code == 200

    r = client.get("/notes/search/", params={"q": "Hello"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    # exercise the new search-by-content endpoint directly
    r = client.get("/notes/search_by_content/")
    assert r.status_code == 200

    r = client.get("/notes/search_by_content/", params={"q": "hello"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    # case-insensitive check
    r = client.get("/notes/search_by_content/", params={"q": "HELLO"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1
