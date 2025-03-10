from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Unit_Concept(Base):
    __tablename__ = "unit_concept"
    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(ForeignKey('unit.id'))
    concept_id = Column(ForeignKey('concept.id'))
