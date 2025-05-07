from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from _models.base import Base

class Prep(Base):
    __tablename__ = "prep"
    id = Column(Integer, primary_key=True, index=True)
    color = Column(Text(10))
    subject_id = Column(Integer, ForeignKey('subject.id'))
    grade_level = Column(Text(255))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))

    subject = relationship("Subject") 
    # classes = relationship("ClassModel", secondary="class_prep", back_populates="preps")


    # class_ = relationship("ClassModel", backref="subjects") 



