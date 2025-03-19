from sqlmodel import SQLModel, Field
from typing import Optional

class AssignConcept(SQLModel, table=True):
    __tablename__ = "assign_concept"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    concept_id: int = Field(foreign_key="concept.id")
    assign_id: int = Field(foreign_key="assign.id")
