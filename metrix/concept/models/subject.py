from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from _models.base import Base

class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255))
    is_global = Column(Boolean, default=False)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=True) 
    grade_min = Column(Integer, default=0)
    grade_max = Column(Integer, default=13)