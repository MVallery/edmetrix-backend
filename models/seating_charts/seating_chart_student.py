from sqlalchemy import Column, Integer, Text, ForeignKey
from ..base import Base

class Layout(Base):
  __tablename__ = "layout"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(Text(255))
  user_id = ForeignKey('user.id')
  created_at = Column(Text(255))

