from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from _models.base import Base

class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255))
    color = Column(Text(10))
    is_global = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id')) 