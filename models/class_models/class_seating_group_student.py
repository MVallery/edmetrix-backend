from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey, JSON
from ..base import Base

class Class_Seating_Group_Student(Base):
    __tablename__ = "class_seating_group_student"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(ForeignKey('student.id'))
    class_seating_group_id = Column(ForeignKey('class_seating_group.id'))
    order = Column(Integer)