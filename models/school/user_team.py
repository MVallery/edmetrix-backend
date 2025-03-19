from sqlmodel import SQLModel, Field
from typing import Optional

class UserTeam(SQLModel, table=True):
    __tablename__ = "user_team"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    team_id: int = Field(foreign_key="team.id")
    user_id: int = Field(foreign_key="user.id")
