from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class ConceptStandard(Base):
    __tablename__ = "concept_standard"
    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(Integer, ForeignKey('concept.id'))
    standard_id = Column(Integer, ForeignKey('standard.id'))