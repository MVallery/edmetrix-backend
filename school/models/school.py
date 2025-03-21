from sqlalchemy import Column, Integer, Text
from _models.base import Base

class School(Base):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255))
    img = Column(Text(255))
    color = Column(Text(10))