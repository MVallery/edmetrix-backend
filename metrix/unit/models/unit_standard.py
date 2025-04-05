from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class UnitStandard(Base):
    __tablename__ = "unit_standard"
    id = Column(Integer, primary_key=True, index=True)
    standard_id = Column(Integer, ForeignKey('standard.id'))
    unit_id = Column(Integer, ForeignKey('unit.id'))