from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Metric(Base):
    __tablename__ = "metric"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Text(255)) # warm up, spiral, exit ticket, whiteboard,
    teacher_id = Column(ForeignKey('teacher.id'))
    team_id = Column(ForeignKey('team.id'))
    unit_id = Column(ForeignKey('unit.id'))
    concept_id = Column(ForeignKey('concept.id'))
    notes = Column(Text(255))
    date = Column(Text(255))

