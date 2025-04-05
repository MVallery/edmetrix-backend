from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON, DateTime
from _models.base import Base

class ClassNote(Base):
    __tablename__ = "class_note"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text(255))
    order = Column(Integer)
    class_id = Column(Integer, ForeignKey('class.id'))
    created = Column(DateTime)
    updated = Column(DateTime)
    type = Column(Text(255)) # academic / behavior / general