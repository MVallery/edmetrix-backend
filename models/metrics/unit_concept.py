from sqlmodel import SQLModel, Field

class UnitConcept(SQLModel, table=True):
    __tablename__ = "unit_concept"
    id: int = Field(default=None, primary_key=True, index=True)
    unit_id: int = Field(foreign_key="unit.id")
    concept_id: int = Field(foreign_key="concept.id")
