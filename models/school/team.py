from sqlalchemy import Column, Integer, Text, ForeignKey
from ..base import Base

class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, index=True)
    school_id = ForeignKey('school.id')
    team_admin_id = ForeignKey('user.id')
    img = Column(Text(255))
    color = Column(Text(10))