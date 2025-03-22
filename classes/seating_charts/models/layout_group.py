from sqlmodel import SQLModel, Field
from typing import Optional
# FUTURE: implement this to allow teacher to select students and assign them to a group, this will allow things like group points/ group color etc.
class LayoutGroup(SQLModel, table=True):
    __tablename__ = "layout_group"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    layout_id: int = Field(foreign_key="layout.id")
    name: str
    color: Optional[str] = Field(default=None, max_length=10)
