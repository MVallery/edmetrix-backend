from sqlmodel import SQLModel, Field
from typing import Optional, Dict

class Class_Subject(SQLModel, table=True):
    __tablename__ = "class_subject"
    id: Optional[int] = Field(default=None, primary_key=True)
    color: Optional[str] = Field(max_length=10)
    name: str = Field(max_length=255) # later connect to subject table
    color: Optional[str] = Field(max_length=10)
