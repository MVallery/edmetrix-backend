from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class StudentMetric(Base):
    __tablename__ = "student_metric"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    metric_id = Column(Integer, ForeignKey('metric.id'))
    mistake_id = Column(Integer, ForeignKey('mistake.id'))