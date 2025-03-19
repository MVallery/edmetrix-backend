from sqlmodel import SQLModel, Field

class ConceptStandard(SQLModel, table=True):
    __tablename__ = "concept_standard"
    id: int = Field(default=None, primary_key=True, index=True)
    concept_id: int = Field(foreign_key="concept.id")
    standard_id: int = Field(foreign_key="standard.id")
