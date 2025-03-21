from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class Metric(Base):
    __tablename__ = "metric"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Text(255)) # warm up, spiral, exit ticket, whiteboard,
    teacher_id = Column(Integer, ForeignKey('users.id'))
    team_id = Column(Integer, ForeignKey('team.id'))
    unit_id = Column(Integer, ForeignKey('unit.id'))
    concept_id = Column(Integer, ForeignKey('concept.id'))
    notes = Column(Text(255))
    date = Column(Text(255))