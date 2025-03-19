from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class SpiralConcept(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    concept_id: Optional[int] = Field(foreign_key="concept.id")
    assign_id: Optional[int] = Field(foreign_key="assign.id")
