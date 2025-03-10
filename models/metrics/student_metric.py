from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Student_Metric(Base):
    __tablename__ = "student_metric"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(ForeignKey('student.id'))
    metric_id = Column(ForeignKey('metric.id'))
    mistake_id = Column(ForeignKey('mistake.id'))
