from sqlmodel import Field, SQLModel
from typing import Optional

class GroupNote(SQLModel, table=True):
    __tablename__ = "group_note"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    text: Optional[str] = Field(default=None, max_length=255)
    order: Optional[int] = None
    group_id: Optional[int] = Field(default=None, foreign_key="group.id")
    created: Optional[str] = Field(default=None, max_length=255)
    updated: Optional[str] = Field(default=None, max_length=255)
    type: Optional[str] = Field(default=None, max_length=255)  # academic / behavior / general