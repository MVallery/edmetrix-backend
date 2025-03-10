from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey, JSON
from ..base import Base

class Class_Seating(Base):
    __tablename__ = "class_seating"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255)) # group 1 / row 1 / pair 1 The Owls
    order = Column(Integer)
    note = Column(Text(255))
    color = Column(Text(10))
