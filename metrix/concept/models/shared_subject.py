from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from _models.base import Base

class SharedSubject(Base):
    __tablename__ = "shared_subject"
    id = Column(Integer, primary_key=True, index=True)
    color = Column(Text(10))
    subject_id = Column(Integer, ForeignKey('subject.id'))
    grade_level = Column(Text(255))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))

    subject = relationship("Subject") 


    # class_ = relationship("ClassModel", backref="subjects") 



