from datetime import datetime

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str = Field(..., max_length=255)
    content: str = Field(..., min_length=1, max_length=10000)


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NotePatch(BaseModel):
    title: str | None = Field(None, max_length=255)
    content: str | None = Field(None, min_length=1, max_length=10000)


class ActionItemCreate(BaseModel):
    description: str = Field(..., min_length=1, max_length=10000)


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ActionItemPatch(BaseModel):
    description: str | None = Field(None, min_length=1, max_length=10000)
    completed: bool | None = None

