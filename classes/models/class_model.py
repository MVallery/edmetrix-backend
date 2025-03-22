from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from _models.base import Base
 
class ClassModel(Base):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True, index=True)
    order = Column(Integer)
    name = Column(Text(255))
    color = Column(Text(10))
    archived = Column(Boolean)
    grade = Column(JSON)
    grade_min = Column(Integer)
    grade_max = Column(Integer)
    # teacher_id = Column(Integer, ForeignKey('users.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    school_year = Column(Text(9))
