from __future__ import annotations

from pathlib import Path
from typing import List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from . import db
from .db import init_db
from .routers import action_items, notes
from .schemas import NoteWithItemsResponse, ActionItemResponse

init_db()

app = FastAPI(title="Action Item Extractor")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    html_path = Path(__file__).resolve().parents[1] / "frontend" / "index.html"
    return html_path.read_text(encoding="utf-8")


app.include_router(notes.router)
app.include_router(action_items.router)


@app.get("/notes", response_model=List[NoteWithItemsResponse])
def list_notes() -> List[NoteWithItemsResponse]:
    rows = db.list_notes()
    notes_with_items: List[NoteWithItemsResponse] = []
    for row in rows:
        items_rows = db.list_action_items(note_id=row["id"])
        items = [
            ActionItemResponse(
                id=item_row["id"],
                note_id=item_row["note_id"],
                text=item_row["text"],
                done=bool(item_row["done"]),
                created_at=item_row["created_at"],
            )
            for item_row in items_rows
        ]
        notes_with_items.append(
            NoteWithItemsResponse(
                id=row["id"],
                content=row["content"],
                created_at=row["created_at"],
                items=items,
            )
        )
    return notes_with_items


static_dir = Path(__file__).resolve().parents[1] / "frontend"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")