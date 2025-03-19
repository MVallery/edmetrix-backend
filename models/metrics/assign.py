from sqlmodel import SQLModel, Field
from typing import Optional

class Assign(SQLModel, table=True):
    __tablename__ = "assign"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=100)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    teacher_id: Optional[int] = Field(default=None, foreign_key="user.id")
    unit_id: Optional[int] = Field(default=None, foreign_key="unit.id")
    date: Optional[str] = Field(default=None, max_length=100)
    date_created: Optional[str] = Field(default=None, max_length=100)
    status: Optional[str] = Field(default=None, max_length=100)  # active, complete, archived
