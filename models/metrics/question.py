from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    text = Column(Text(255))
    answer = Column(Text(255))
    is_multiple_choice = Column(Boolean)
    assignment_id = Column(ForeignKey('assignment.id'))
    concept_id = Column(ForeignKey('concept.id'))
