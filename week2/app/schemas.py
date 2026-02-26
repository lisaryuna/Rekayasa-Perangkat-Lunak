from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class NoteCreate(BaseModel):
    content: str


class NoteResponse(BaseModel):
    id: int
    content: str
    created_at: str


class ActionItemResponse(BaseModel):
    id: int
    note_id: Optional[int]
    text: str
    done: bool
    created_at: str


class ActionItemsExtractRequest(BaseModel):
    text: str
    save_note: bool = False


class ActionItemsExtractResponse(BaseModel):
    note_id: Optional[int]
    items: List[ActionItemResponse]


class ActionItemDoneRequest(BaseModel):
    done: bool = True


class NoteWithItemsResponse(BaseModel):
    id: int
    content: str
    created_at: str
    items: List[ActionItemResponse]


