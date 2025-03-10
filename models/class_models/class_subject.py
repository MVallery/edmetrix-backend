from sqlalchemy import Column, Integer, Text
from ..base import Base

class Class_Subject(Base):
    __tablename__ = "class_subject"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255))
    color = Column(Text(10))