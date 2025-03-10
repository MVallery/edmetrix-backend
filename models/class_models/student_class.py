from sqlalchemy import Column, Integer, Text, ForeignKey
from ..base import Base

class Student_Class(Base):
    __tablename__ = "student_class"
    id = Column(Integer, primary_key=True, index=True)
    order = Column(Integer)
    class_id = Column(ForeignKey('class.id'))
    student_id = Column(ForeignKey('student.id'))
    color = Column(Text(10))