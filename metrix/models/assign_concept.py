from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class AssignConcept(Base):
    __tablename__ = "assign_concept"
    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(Integer, ForeignKey('concept.id'))
    assign_id = Column(Integer, ForeignKey('assign.id'))