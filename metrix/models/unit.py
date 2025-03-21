from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text(255))
    description = Column(Text)
    # created_by is in case it was made by another user to keep track
    # team_id is in case the team generates a Unit and is sharing it so when edited it will be edited for all
    # user_id is in case this is a user specific unit that they want outside of a team.
    created_by = Column(Integer, ForeignKey('users.id'))
    team_id = Column(Integer, ForeignKey('team.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    is_premade = Column(Boolean)
    color = Column(Text(10))