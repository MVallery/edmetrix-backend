from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON, Date
from _models.base import Base
 
class ClassMetric(Base):
    __tablename__ = "class_metric"
    id = Column(Integer, primary_key=True, index=True)
    metric_id = Column(Integer, ForeignKey('metric.id'))
    class_id = Column(Integer, ForeignKey('class.id'))
    date = Column(Date)

