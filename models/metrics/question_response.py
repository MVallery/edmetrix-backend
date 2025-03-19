from sqlmodel import SQLModel, Field

class QuestionResponse(SQLModel, table=True):
    __tablename__ = "question_response"
    id: int = Field(default=None, primary_key=True, index=True)
    question_id: int = Field(foreign_key="question.id")
    student_id: int = Field(foreign_key="student.id")
    mistake_id: int = Field(foreign_key="mistake.id")
    text: str = Field(max_length=255)
