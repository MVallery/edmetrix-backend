from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from _models.base import Base
# Current concepts tagged for that particular group to work on
class GroupConcept(Base):
    __tablename__ = "group_concept"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    concept_id = Column(Integer, ForeignKey('concept.id'))