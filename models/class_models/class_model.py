from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ..base import Base

class Class_Model(Base):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True, index=True)
    order = Column(Integer)
    name = Column(Text(255))
    color = Column(Text(10))
    archived = Column(Boolean)
    grade = Column(JSON)
    grade_min = Column(Integer)
    grade_max = Column(Integer)
    teacher_id = ForeignKey('teacher.id')
    school_year = Column(Text(9))

    # Optional: Define a relationship to access teacher details automatically
    # teacher = relationship('Teacher')
