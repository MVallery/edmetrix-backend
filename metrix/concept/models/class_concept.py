from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from _models.base import Base

class ClassConcept(Base):
  __tablename__ = "class_concept"
  id = Column(Integer, primary_key=True, index=True)
  class_id = Column(Integer, ForeignKey('class.id'))
  concept_id = Column(Integer, ForeignKey('concept.id'))
  subject_id = Column(Integer, ForeignKey('subject.id'))
  active = Column(Boolean, default=True) # Concept is actively being used in this class

  concept = relationship("Concept") 
  class_ = relationship("ClassModel", backref="concepts") 
  class_subject = relationship("ClassSubject", backref="concepts")




