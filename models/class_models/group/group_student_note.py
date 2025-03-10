from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ...base import Base

class Group_Student_Note(Base):
    __tablename__ = "group_student_note"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text(255))
    order = Column(Integer)
    group_id = Column(ForeignKey('group.id'))
    created = Column(Text(255))
    updated = Column(Text(255))
    type = Column(Text(255)) # academic / behavior / general