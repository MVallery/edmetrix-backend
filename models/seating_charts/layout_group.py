from sqlmodel import SQLModel, Field
from typing import Optional
# Blank Seat positions in the layout that students can be dragged to
class LayoutGroup(SQLModel, table=True):
    __tablename__ = "layout_group"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    layout_id: int = Field(foreign_key="layout.id")
    name: str
    color: Optional[str] = Field(default=None, max_length=10)
