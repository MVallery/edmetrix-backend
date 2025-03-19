from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum as PyEnum

class ChartStatus(str, PyEnum):
  active = "active"
  inactive = "inactive"
  archived = "archived"

class Layout(SQLModel, table=True):
  __tablename__ = "layout"

  id: Optional[int] = Field(default=None, primary_key=True, index=True)
  name: str
  user_id: int = Field(foreign_key="user.id")
  created_at: Optional[str] = Field(default=None)
  status: ChartStatus = Field(default=ChartStatus.inactive)
  rows: int
  cols: int
