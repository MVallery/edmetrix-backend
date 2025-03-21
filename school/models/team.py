from sqlalchemy import Column, Integer, Text, ForeignKey
from _models.base import Base

class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey('school.id'))
    team_admin_id = Column(Integer, ForeignKey('users.id'))
    img = Column(Text(255))
    color = Column(Text(10))