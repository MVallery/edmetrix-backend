from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from _models.base import Base

class GroupStudentNote(Base):
    __tablename__ = "group_student_note"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text(255))
    order = Column(Integer)
    group_id = Column(Integer, ForeignKey('group.id'))
    created = Column(Text(255))
    updated = Column(Text(255))
    type = Column(Text(255)) # academic / behavior / general