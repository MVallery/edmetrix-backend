from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ..base import Base

class Class_Note(Base):
    __tablename__ = "class_note"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text(255))
    order = Column(Integer)
    class_id = Column(ForeignKey('class.id'))
    created = Column(Text(255))
    updated = Column(Text(255))
    type = Column(Text(255)) # academic / behavior / general