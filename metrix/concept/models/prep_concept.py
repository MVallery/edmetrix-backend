from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from _models.base import Base

class PrepConcept(Base):
  __tablename__ = "prep_concept"
  id = Column(Integer, primary_key=True, index=True)
  concept_id = Column(Integer, ForeignKey('concept.id'))
  prep_id = Column(Integer, ForeignKey('prep.id'))
  active = Column(Boolean, default=True) # Concept is actively being used in this class

  concept = relationship("Concept") 
  prep = relationship("Prep", backref="concepts")
  created_at = Column(DateTime, default=func.now())




