from sqlalchemy import Column, Integer, Text, ForeignKey, Enum
from typing import Optional
from _models.base import Base

class LayoutDesk(Base):
  __tablename__ = "layout_desk"

  id = Column(Integer, primary_key=True, index=True)
  layout_id = Column(ForeignKey("layout.id"))
  col = Column(Integer)
  row = Column(Integer)
