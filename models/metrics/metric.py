from sqlmodel import SQLModel, Field
from typing import Optional

class Metric(SQLModel, table=True):
    __tablename__ = "metric"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    type: Optional[str] = Field(max_length=255)  # warm up, spiral, exit ticket, whiteboard
    teacher_id: Optional[int] = Field(foreign_key="user.id")
    team_id: Optional[int] = Field(foreign_key="team.id")
    unit_id: Optional[int] = Field(foreign_key="unit.id")
    concept_id: Optional[int] = Field(foreign_key="concept.id")
    notes: Optional[str] = Field(max_length=255)
    date: Optional[str] = Field(max_length=255)
