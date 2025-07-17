from sqlalchemy import Column, Integer, Text, ForeignKey, String
from _models.base import Base

class UserTeam(Base):
    __tablename__ = "user_team"
    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey('team.id'))
    user_id = Column(String(36), ForeignKey('user.id'))

