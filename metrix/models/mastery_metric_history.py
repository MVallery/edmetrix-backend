from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from _models.base import Base

# overall metric history, allows us to easily track changes over time.

class MasteryMetricHistory(Base):
    __tablename__ = "mastery_metric_history"
    id = Column(Integer, primary_key=True, index=True)
    mastery_metric_id = Column(Integer, ForeignKey('mastery_metric.id'))
    notes = Column(Text(1000))
    old_level = Column(Integer) # 1-4 for those scaled metrics (MVP), 0 - 100 for percentage metrics 
    new_level = Column(Integer) # 1-4 for those scaled metrics (MVP), 0 - 100 for percentage metrics
    class_id = Column(Integer, ForeignKey('class.id'))
    date = Column(DateTime, default=func.now())


