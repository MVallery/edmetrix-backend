from sqlalchemy import Column, Integer, Text, ForeignKey
from _models.base import Base

class StudentNote(Base):
    __tablename__ = "student_note"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    text = Column(Text(255))
    color = Column(Text(10))