from sqlmodel import SQLModel, Field
from typing import Optional

class LayoutSeat(SQLModel, table=True):
  __tablename__ = "layout_seat"

  id: Optional[int] = Field(default=None, primary_key=True, index=True)
  layout_id: int = Field(foreign_key="layout.id")
  col: int
  row: int
  layout_group_id: Optional[int] = Field(default=None, foreign_key="layout_group.id")
