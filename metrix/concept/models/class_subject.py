from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from _models.base import Base

class ClassSubject(Base):
    __tablename__ = "class_subject"
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey('class.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))
    color = Column(Text(10))

    subject = relationship("Subject") 

    class_ = relationship("ClassModel", backref="subjects") 


