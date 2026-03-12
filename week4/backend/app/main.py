from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Depends

from .db import apply_seed_if_needed, engine, get_db
from .models import Base, Note
from .routers import action_items as action_items_router
from .routers import notes as notes_router
from .schemas import NoteRead
from sqlalchemy import select
from sqlalchemy.orm import Session

app = FastAPI(title="Modern Software Dev Starter (Week 4)")

# Ensure data dir exists
Path("data").mkdir(parents=True, exist_ok=True)

# Mount static frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.on_event("startup")
def startup_event() -> None:
    Base.metadata.create_all(bind=engine)
    apply_seed_if_needed()


@app.get("/")
async def root() -> FileResponse:
    return FileResponse("frontend/index.html")


# Routers
app.include_router(notes_router.router)
app.include_router(action_items_router.router)


# standalone search-by-content endpoint (new feature)
@app.get("/notes/search_by_content/", response_model=list[NoteRead])
def search_notes_content(q: str | None = None, db: Session = Depends(get_db)) -> list[NoteRead]:
    """Search notes by **content** only (case‑insensitive).

    This mirrors the existing router-based search but lives in `main.py` as requested.
    """
    if not q:
        rows = db.execute(select(Note)).scalars().all()
    else:
        # use ilike for case‑insensitive matching
        rows = (
            db.execute(select(Note).where(Note.content.ilike(f"%{q}%")))
            .scalars()
            .all()
        )
    return [NoteRead.model_validate(row) for row in rows]
