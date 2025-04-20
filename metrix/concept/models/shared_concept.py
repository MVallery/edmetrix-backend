from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from _models.base import Base

class SharedConcept(Base):
  __tablename__ = "shared_concept"
  id = Column(Integer, primary_key=True, index=True)
  concept_id = Column(Integer, ForeignKey('concept.id'))
  shared_subject_id = Column(Integer, ForeignKey('shared_subject.id'))
  active = Column(Boolean, default=True) # Concept is actively being used in this class

  concept = relationship("Concept") 
  shared_subject = relationship("SharedSubject", backref="concepts")




