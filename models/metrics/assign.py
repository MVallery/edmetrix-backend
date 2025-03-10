from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Assign(Base):
    __tablename__ = "assign_result"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text(100))
    description = Column(Text(100))
    team_id = Column(ForeignKey('team.id'))
    teacher_id = Column(ForeignKey('teacher.id'))
    unit_id = Column(ForeignKey('unit.id'))
    date = Column(Text(100))
    date_created = Column(Text(100))
    status = Column(Text(100)) # active # complete # archived 


