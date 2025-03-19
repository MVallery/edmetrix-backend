from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class Concept(SQLModel, table=True):
    __tablename__ = "concept"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    parent_concept_id: Optional[int] = Field(default=None, foreign_key="concept.id")
    name: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = Field(default=None, max_length=255)
