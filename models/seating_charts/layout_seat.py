from sqlalchemy import Column, Integer, Text, ForeignKey
from ..base import Base
# Blank Seat positions in the layout that students can be dragged to
class LayoutSeat(Base):
  __tablename__ = "layout_seat"
  id = Column(Integer, primary_key=True, index=True)
  layout_id = ForeignKey('layout.id')
  x = Column(Integer)
  y = Column(Integer)
  layout_group_id = Column(ForeignKey('layout_group.id'))
