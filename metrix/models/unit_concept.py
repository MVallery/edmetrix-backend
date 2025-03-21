from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class UnitConcept(Base):
    __tablename__ = "unit_concept"
    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    concept_id = Column(Integer, ForeignKey('concept.id'))