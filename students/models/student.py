from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from _models.base import Base

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(Text(255))
    last_name = Column(Text(255))
    name = Column(Text(255))
    email = Column(Text(255))
    birthday = Column(Text(255))
    img = Column(Text(255))
    grade_level = Column(Integer)
    school_student_id = Column(Text(255), nullable=True) # ID used by the school system, if applicable
    school_id = Column(Integer, ForeignKey("school.id"))
    gender = Column(Text(1), nullable=True) # M, F, O
    active = Column(Boolean, default=True) # if student is active in this class/school
