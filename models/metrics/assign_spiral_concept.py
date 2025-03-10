from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Spiral_Concept(Base):
    __tablename__ = "spiral_concept"
    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(ForeignKey('concept.id'))
    assign_id = Column(ForeignKey('assign.id'))

