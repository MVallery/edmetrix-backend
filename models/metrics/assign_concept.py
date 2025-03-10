from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Assign_Concept(Base):
    __tablename__ = "assign_concept"
    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(ForeignKey('concept.id'))
    assign_id = Column(ForeignKey('assign.id'))

