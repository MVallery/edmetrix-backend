from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ...base import Base
# Current concepts tagged for that particular group to work on
class Group_Concept(Base):
    __tablename__ = "group_concept"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(ForeignKey('group.id'))
    concept_id = Column(ForeignKey('concept.id'))