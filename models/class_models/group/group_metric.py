from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ...base import Base

class Group_Metric(Base):
    __tablename__ = "group_metric"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255))
    description = Column(Text(255))
    group_id = Column(ForeignKey('group.id'))
    unit_id = Column(ForeignKey('unit.id'))
    concept_id = Column(ForeignKey('concept.id'))
    notes = Column(Text(255))
    date = Column(Text(255))
