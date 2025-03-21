from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class Concept(Base):
    __tablename__ = "concept"
    id = Column(Integer, primary_key=True, index=True)
    parent_concept_id = Column(Integer, ForeignKey('concept.id'))
    name = Column(Text(255))
    description = Column(Text(255))