from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey, JSON
from ..base import Base

class Class_Seating(Base):
    __tablename__ = "class_seating"
    id = Column(Integer, primary_key=True, index=True)
    order = Column(Integer)
    status = Column(Text(255)) # active / inactive
    active_starting = Column(Text(255)) # date
    active_ending = Column(Text(255)) # date
    type = Column(Text(255)) # rows, groups, pairs
    