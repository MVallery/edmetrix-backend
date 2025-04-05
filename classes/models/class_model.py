from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from _models.base import Base
 
class ClassModel(Base):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True, index=True)
    order = Column(Integer)
    name = Column(Text(255))
    # TO DO: Add this functionality in so teachers can organize classes into groups maybe should be separate table
    # would be able to add this in to the teacher_context table to let them set the active concept per category.
    # category = Column(Text(255))
    color = Column(Text(10))
    archived = Column(Boolean)
    grade = Column(JSON)
    grade_min = Column(Integer)
    grade_max = Column(Integer)
    # teacher_id = Column(Integer, ForeignKey('users.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    school_year = Column(Text(9))


