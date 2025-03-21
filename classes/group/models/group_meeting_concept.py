from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from _models.base import Base

class GroupMeetingConcept(Base):
    __tablename__ = "group_meeting_concept"
    id = Column(Integer, primary_key=True, index=True)
    group_meeting_id = Column(Integer, ForeignKey('group_meeting.id'))
    concept_id = Column(Integer, ForeignKey('concept.id'))