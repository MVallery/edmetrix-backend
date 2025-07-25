from sqlalchemy import Column, Integer, Text, Boolean
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
    active = Column(Boolean, default=True) # if student is active in this class or not 
