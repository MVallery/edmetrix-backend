from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Concept_Standard(Base):
    __tablename__ = "concept_standard"
    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(ForeignKey('concept.id'))
    standard_id = Column(ForeignKey('standard.id'))
