from sqlalchemy import Column, Integer, Text, ForeignKey
from ..base import Base
# Blank Seat positions in the layout that students can be dragged to
class LayoutGroup(Base):
  __tablename__ = "layout_group"
  id = Column(Integer, primary_key=True, index=True)
  layout_id = ForeignKey('layout.id')
  name = Column(Text(255))
  color = Column(Text(10))

