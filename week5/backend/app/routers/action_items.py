from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import ActionItem
from ..schemas import ActionItemCreate, ActionItemRead, PaginatedResponse, SuccessEnvelope

router = APIRouter(prefix="/action-items", tags=["action_items"])


@router.get("/", response_model=SuccessEnvelope[PaginatedResponse[ActionItemRead]])
def list_items(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    total: int = db.execute(select(func.count()).select_from(ActionItem)).scalar_one()
    offset = (page - 1) * page_size
    rows = db.execute(select(ActionItem).offset(offset).limit(page_size)).scalars().all()
    return {"ok": True, "data": PaginatedResponse(items=[ActionItemRead.model_validate(r) for r in rows], total=total)}


@router.post("/", response_model=SuccessEnvelope[ActionItemRead], status_code=201)
def create_item(payload: ActionItemCreate, db: Session = Depends(get_db)):
    item = ActionItem(description=payload.description, completed=False)
    db.add(item)
    db.flush()
    db.refresh(item)
    return {"ok": True, "data": ActionItemRead.model_validate(item)}


@router.put("/{item_id}/complete", response_model=SuccessEnvelope[ActionItemRead])
def complete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.get(ActionItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Action item not found")
    item.completed = True
    db.add(item)
    db.flush()
    db.refresh(item)
    return {"ok": True, "data": ActionItemRead.model_validate(item)}
