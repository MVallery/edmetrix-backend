from sqlalchemy import Column, Integer, Text, ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import relationship
from _models.base import Base
from pydantic import BaseModel
from typing import List, Optional
from .layout_desk import LayoutDeskSchema

class Layout(Base):
  __tablename__ = "layout"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(Text(255))
  teacher_id = Column(Integer, ForeignKey('teacher.id'))
  created_at = Column(DateTime, default=func.now())
  status = Column(Enum('active', 'inactive', 'archived', name='chart_status_enum'), default='inactive')

  # Just keeps track of the number of rows and columns in the layout so we can easily know how to set up the classroom.
  rows = Column(Integer)
  cols = Column(Integer)

  desks = relationship("LayoutDesk")


class LayoutSchema(BaseModel):
  id: int
  name: str
  teacher_id: int
  status: str
  rows: int
  cols: int
  desks: List[LayoutDeskSchema]

  class Config:
    orm_mode = True