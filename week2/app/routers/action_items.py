from __future__ import annotations

from typing import List, Optional

from fastapi import APIRouter, HTTPException

from .. import db
from ..schemas import (
    ActionItemDoneRequest,
    ActionItemResponse,
    ActionItemsExtractRequest,
    ActionItemsExtractResponse,
)
from ..services.extract import extract_action_items_llm


router = APIRouter(prefix="/action-items", tags=["action-items"])


@router.post("/extract", response_model=ActionItemsExtractResponse)
def extract(payload: ActionItemsExtractRequest) -> ActionItemsExtractResponse:
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    note_id: Optional[int] = None
    if payload.save_note:
        note_id = db.insert_note(text)

    try:
        items = extract_action_items_llm(text)
    except Exception as exc:  # pragma: no cover - defensive, in case LLM errors surface
        raise HTTPException(status_code=500, detail="Failed to extract action items") from exc

    ids = db.insert_action_items(items, note_id=note_id)

    # Re-load action items to get accurate created_at/done values from DB
    rows = db.list_action_items(note_id=note_id) if note_id is not None else db.list_action_items()
    by_id = {int(r["id"]): r for r in rows}
    response_items: List[ActionItemResponse] = []
    for i in ids:
        row = by_id.get(int(i))
        if row is None:
            continue
        response_items.append(
            ActionItemResponse(
                id=row["id"],
                note_id=row["note_id"],
                text=row["text"],
                done=bool(row["done"]),
                created_at=row["created_at"],
            )
        )

    return ActionItemsExtractResponse(note_id=note_id, items=response_items)


@router.get("", response_model=List[ActionItemResponse])
def list_all(note_id: Optional[int] = None) -> List[ActionItemResponse]:
    rows = db.list_action_items(note_id=note_id)
    return [
        ActionItemResponse(
            id=r["id"],
            note_id=r["note_id"],
            text=r["text"],
            done=bool(r["done"]),
            created_at=r["created_at"],
        )
        for r in rows
    ]


@router.post("/{action_item_id}/done")
def mark_done(action_item_id: int, payload: ActionItemDoneRequest) -> dict:
    done = bool(payload.done)
    try:
        db.mark_action_item_done(action_item_id, done)
    except Exception as exc:  # pragma: no cover - defensive 500
        raise HTTPException(status_code=500, detail="Failed to update action item") from exc
    return {"id": action_item_id, "done": done}


