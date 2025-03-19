
from sqlmodel import SQLModel, Field
from typing import Optional

class StudentClass(SQLModel, table=True):
    __tablename__ = "student_class"

    id: Optional[int] = Field(default=None, primary_key=True)
    order: Optional[int]
    class_id: int = Field(foreign_key="class.id")
    student_id: int = Field(foreign_key="student.id")
    color: Optional[str] = Field(default=None, max_length=10)

# from sqlalchemy import Column, Integer, Text, ForeignKey
# from ..base import Base

# class Student_Class(Base):
#     __tablename__ = "student_class"
#     id = Column(Integer, primary_key=True, index=True)
#     order = Column(Integer)
#     class_id = Column(ForeignKey('class.id'))
#     student_id = Column(ForeignKey('student.id'))
#     color = Column(Text(10))