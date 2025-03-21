from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from _models.base import Base

class StudentClass(Base):
    __tablename__ = "student_class"
    id = Column(Integer, primary_key=True, index=True)
    order = Column(Integer)
    class_id = Column(Integer, ForeignKey('class.id'))
    student_id = Column(Integer, ForeignKey('student.id'))
    color = Column(Text(10))
    student = relationship("Student", backref="student_classes") # relationship with Student - backref will allow populating student_classes when pulling student. 

