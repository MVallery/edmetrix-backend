from sqlalchemy import Column, Integer, Text, ForeignKey
from ..base import Base

class Student_Note(Base):
    __tablename__ = "student_note"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(ForeignKey('student.id'))
    text = Column(Text(255))
    color = Column(Text(10))