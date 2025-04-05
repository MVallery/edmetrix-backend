from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class Assign(Base):
    __tablename__ = "assign"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text(100))
    description = Column(Text(100))
    team_id = Column(Integer, ForeignKey('team.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    unit_id = Column(Integer, ForeignKey('unit.id'))
    date = Column(Text(100))
    date_created = Column(Text(100))
    status = Column(Text(100)) # active # complete # archived 
