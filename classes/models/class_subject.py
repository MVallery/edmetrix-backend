from sqlalchemy import Column, Integer, Text
from _models.base import Base

class ClassSubject(Base):
    __tablename__ = "class_subject"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255))
    color = Column(Text(10))