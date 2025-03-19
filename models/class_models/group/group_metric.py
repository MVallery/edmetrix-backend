from sqlmodel import SQLModel, Field
from typing import Optional

class GroupMetric(SQLModel, table=True):
    __tablename__ = "group_metric"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = Field(default=None, max_length=255)
    group_id: Optional[int] = Field(default=None, foreign_key="group.id")
    unit_id: Optional[int] = Field(default=None, foreign_key="unit.id")
    concept_id: Optional[int] = Field(default=None, foreign_key="concept.id")
    notes: Optional[str] = Field(default=None, max_length=255)
    date: Optional[str] = Field(default=None, max_length=255)
