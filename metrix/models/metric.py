from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from _models.base import Base

class Metric(Base):
    __tablename__ = "metric"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Text(255)) # warm up, spiral, exit ticket, whiteboard,
    name = Column(Text(255)) # name of the metric like "Add Fractions"
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    team_id = Column(Integer, ForeignKey('team.id'))
    unit_id = Column(Integer, ForeignKey('unit.id'))
    concept_id = Column(Integer, ForeignKey('concept.id'))
    notes = Column(Text(255))
    #  100, 4, 3, 2 (100 will be grade based, the rest will just have a color & map with "Developing/Profificient etc"),
    # If scale is 4 -> options for student level: 4 = advanced, 3 = proficient, 2 = developing, 1 = beginner
    # If scale is 3 -> options for student level: 4, 3, 1
    # If scale is 2 -> options for student level: 4 = adv, 1 = beg
    level_scale = Column(Text(255)) 


