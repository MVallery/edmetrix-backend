from sqlmodel import SQLModel, Field
from typing import Optional, Dict

class Subject(SQLModel, table=True):
    __tablename__ = "subject"
    id: Optional[int]= Field(primary_key=True, index=True)
    name: str = Field(max_length=255)
