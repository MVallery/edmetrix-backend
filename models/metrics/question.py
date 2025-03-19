from sqlmodel import SQLModel, Field

class Question(SQLModel, table=True):
    __tablename__ = "question"
    id: int = Field(default=None, primary_key=True, index=True)
    number: int
    text: str = Field(max_length=255)
    answer: str = Field(max_length=255)
    is_multiple_choice: bool
    assign_id: int = Field(foreign_key="assign.id")
    concept_id: int = Field(foreign_key="concept.id")
