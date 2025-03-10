from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Unit_Standard(Base):
    __tablename__ = "unit_standard"
    id = Column(Integer, primary_key=True, index=True)
    standard_id = Column(ForeignKey('standard.id'))
    unit_id = Column(ForeignKey('unit.id'))
