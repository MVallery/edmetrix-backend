from sqlalchemy import Column, Integer, Text, ForeignKey, Enum
from _models.base import Base

class Layout(Base):
  __tablename__ = "layout"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(Text(255))
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(Text(255))
  status = Column(Enum('active', 'inactive', 'archived', name='chart_status_enum'), default='inactive')
  rows = Column(Integer)
  cols = Column(Integer)