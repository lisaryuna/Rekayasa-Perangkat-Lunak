from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


# ---------------------------------------------------------------------------
# Envelope models
# ---------------------------------------------------------------------------


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorEnvelope(BaseModel):
    ok: bool = False
    error: ErrorDetail


class SuccessEnvelope(BaseModel, Generic[T]):
    ok: bool = True
    data: T


class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    total: int


# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------


class NoteCreate(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)


class NoteRead(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True


# ---------------------------------------------------------------------------
# Action items
# ---------------------------------------------------------------------------


class ActionItemCreate(BaseModel):
    description: str = Field(min_length=1)


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool

    class Config:
        from_attributes = True
