from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship
from _models.base import Base

# overall metric for the student per concept. For MVP, this will be all that is used until we later add in the per-assignment general metrics.
# in this future, we will have a per-assignment metrics that will be used to calculate the overall metric for the student per concept. (But can be overridden by the teacher)
# perhaps taking average of most recent 3 assignments.

class MasteryMetric(Base):
    __tablename__ = "mastery_metric"
    __table_args__ = (
      UniqueConstraint('student_id', 'concept_id', name='uix_master_metric'),
    )
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    concept_id = Column(Integer, ForeignKey('prep_concept.id'))
    class_id = Column(Integer, ForeignKey('class.id'))
    notes = Column(Text(1000))
    level = Column(Integer) # 1-4 for those scaled metrics (MVP), 0 - 100 for percentage metrics 
    date = Column(DateTime, default=func.now())

    concept = relationship("PrepConcept", backref="mastery_metrics")


