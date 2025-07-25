from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey, String
from _models.base import Base
from sqlalchemy.orm import relationship

class Concept(Base):
    __tablename__ = "concept"
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey('subject.id'))
    parent_concept_id = Column(Integer, ForeignKey('concept.id'))
    is_main_concept = Column(Boolean, default=False)
    name = Column(Text(255), nullable=False)
    description = Column(Text(255))
    user_id = Column(String(36), ForeignKey('user.id'))
    is_global = Column(Boolean, default=False)
    grade_level = Column(Text(255)) # main concept like Multiplication may have a range of grade levelssh, but front-end should allow showing prev / next grade levels to account for differences.
    grade_min = Column(Integer, default=0)
    grade_max = Column(Integer, default=13)

    subject = relationship("Subject")
