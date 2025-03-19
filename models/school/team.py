from sqlmodel import SQLModel, Field
from typing import Optional

class Team(SQLModel, table=True):
    __tablename__ = "team"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    school_id: int = Field(foreign_key="school.id")
    team_admin_id: int = Field(foreign_key="user.id")
    img: Optional[str] = Field(default=None)
    color: Optional[str] = Field(default=None, max_length=10)
