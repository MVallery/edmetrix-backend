from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from _models.base import Base

class GroupMetric(Base):
    __tablename__ = "group_metric"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255))
    description = Column(Text(255))
    group_id = Column(Integer, ForeignKey('group.id'))
    unit_id = Column(Integer, ForeignKey('unit.id'))
    concept_id = Column(Integer, ForeignKey('concept.id'))
    notes = Column(Text(255))
    date = Column(Text(255))