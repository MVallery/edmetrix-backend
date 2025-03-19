from sqlmodel import SQLModel, Field
from typing import Optional

class SeatingChartStudent(SQLModel, table=True):
    __tablename__ = "seating_chart_student"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    user_id: int = Field(foreign_key="user.id")
    created_at: Optional[str] = Field(default=None)