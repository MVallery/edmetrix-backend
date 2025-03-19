from sqlmodel import SQLModel, Field
from typing import Optional

class GroupMeeting(SQLModel, table=True):
    __tablename__ = "group_meeting"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    date: Optional[str] = Field(default=None, max_length=255)
    group_id: Optional[int] = Field(default=None, foreign_key="group.id")
    notes: Optional[str] = Field(default=None, max_length=255)
    created: Optional[str] = Field(default=None, max_length=255)
    time: Optional[str] = Field(default=None, max_length=5)
    minutes: Optional[str] = Field(default=None, max_length=2)
