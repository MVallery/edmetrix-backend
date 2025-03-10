from sqlalchemy import Column, Integer, Text, ForeignKey
from ..base import Base

class User_Team(Base):
    __tablename__ = "user_team"
    id = Column(Integer, primary_key=True, index=True)
    team_id = ForeignKey('team.id')
    user_id = ForeignKey('user.id')