from sqlmodel import SQLModel, Field
from typing import Optional, Dict

class Class_Model(SQLModel, table=True):
    __tablename__ = "class"

    id: Optional[int] = Field(default=None, primary_key=True)
    order: Optional[int]
    name: str = Field(max_length=255)
    color: Optional[str] = Field(max_length=10)
    archived: Optional[bool]
    grade: Optional[str]  # JSON as dict
    grade_min: Optional[int]
    grade_max: Optional[int]
    teacher_id: Optional[int] = Field(foreign_key="user.id")
    school_year: Optional[str] = Field(max_length=9)


# from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
# from ..base import Base

# class Class_Model(Base):
#     __tablename__ = "class"
#     id = Column(Integer, primary_key=True, index=True)
#     order = Column(Integer)
#     name = Column(Text(255))
#     color = Column(Text(10))
#     archived = Column(Boolean)
#     grade = Column(JSON)
#     grade_min = Column(Integer)
#     grade_max = Column(Integer)
#     teacher_id = ForeignKey('teacher.id')
#     school_year = Column(Text(9))

#     # Optional: Define a relationship to access teacher details automatically
#     # teacher = relationship('Teacher')
