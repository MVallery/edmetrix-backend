from sqlmodel import Field, SQLModel

# Current concepts tagged for that particular group to work on
class GroupConcept(SQLModel, table=True):
    __tablename__ = "group_concept"
    id: int = Field(default=None, primary_key=True, index=True)
    group_id: int = Field(foreign_key="group.id")
    concept_id: int = Field(foreign_key="concept.id")