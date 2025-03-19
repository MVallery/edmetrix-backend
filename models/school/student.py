from sqlmodel import SQLModel, Field
from typing import Optional

class Student(SQLModel, table=True):
    __tablename__ = "student"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    first_name: str
    last_name: str
    birthday: Optional[str] = Field(default=None)
    img: Optional[str] = Field(default=None)
    grade_level: int
