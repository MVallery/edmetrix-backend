from sqlmodel import SQLModel, Field
from typing import Optional

class School(SQLModel, table=True):
    __tablename__ = "school"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    img: Optional[str] = Field(default=None)
    color: Optional[str] = Field(default=None, max_length=10)
