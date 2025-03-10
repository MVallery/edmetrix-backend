from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ...base import Base

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Text(255)) # active / inactive
    name = Column(Text(255))
    description = Column(Text(255))
    class_id = Column(ForeignKey('class.id'))