
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional


class AssignResult(SQLModel, table=True):
    __tablename__: str = "assign_result"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    assign_id: Optional[int] = Field(foreign_key="assign.id")
    student_id: Optional[int] = Field(foreign_key="student.id")
    score: Optional[int] = Field(default=None)
    status: Optional[str] = Field(default=None, max_length=100)  # complete, incomplete, not_started, retest
    retest_score: Optional[int] = Field(default=None)
    retest_status: Optional[str] = Field(default=None, max_length=100)  # complete, incomplete, not_started