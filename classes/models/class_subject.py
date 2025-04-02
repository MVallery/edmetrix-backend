from sqlalchemy import Column, Integer, Text
from _models.base import Base

class ClassSubject(Base):
    __tablename__ = "class_subject"
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, index=True)
    subject_id = Column(Integer, index=True)
    color = Column(Text(10))