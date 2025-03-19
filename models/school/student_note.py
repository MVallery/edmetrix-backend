from sqlmodel import SQLModel, Field
from typing import Optional

class StudentNote(SQLModel, table=True):
    __tablename__ = "student_note"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    student_id: int = Field(foreign_key="student.id")
    text: str
    color: Optional[str] = Field(default=None, max_length=10)
