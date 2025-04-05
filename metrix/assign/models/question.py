from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    text = Column(Text(255))
    answer = Column(Text(255))
    is_multiple_choice = Column(Boolean)
    assign_id = Column(Integer, ForeignKey('assign.id'))
    concept_id = Column(Integer, ForeignKey('concept.id'))
    # metric_id = Column(Integer, ForeignKey('metric.id'))