from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ...base import Base

class Group_Meeting_Concept(Base):
    __tablename__ = "group_meeting_concept"
    id = Column(Integer, primary_key=True, index=True)
    group_meeting_id = Column(ForeignKey('group_meeting.id'))
    concept_id = Column(ForeignKey('concept.id'))
