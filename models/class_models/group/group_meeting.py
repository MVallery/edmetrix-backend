from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ...base import Base

class Group_Meeting(Base):
    __tablename__ = "group_meeting"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Text(255))
    group_id = Column(ForeignKey('group.id'))
    notes = Column(Text(255))
    created = Column(Text(255))
    time = Column(Text(5))
    minutes = Column(Text(2))
