from sqlmodel import Field, SQLModel
from typing import Optional

class Unit(SQLModel, table=True):
    __tablename__ = "unit"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = None
    
    # created_by is in case it was made by another user to keep track
    created_by: Optional[int] = Field(default=None, foreign_key="user.id")
    
    # team_id is in case the team generates a Unit and is sharing it so when edited it will be edited for all
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    
    # user_id is in case this is a user specific unit that they want outside of a team.
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    
    is_premade: Optional[bool] = None
    color: Optional[str] = Field(default=None, max_length=10)