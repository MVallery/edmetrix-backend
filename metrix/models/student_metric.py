from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from _models.base import Base

class StudentMetric(Base):
    __tablename__ = "student_metric"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    metric_id = Column(Integer, ForeignKey('metric.id'))
    mistake_id = Column(Integer, ForeignKey('mistake.id'))
    class_id = Column(Integer, ForeignKey('class.id'))
    student_class_id = Column(Integer, ForeignKey('student_class.id')) #may only need this in future, but want to include others in case it helps
    note = Column(Text(1000))
    level = Column(Integer) # 1-4 for those scaled metrics, 0 - 100 for percentage metrics, each will map to the 

    student_class= relationship("StudentClass", backref="student_metrics") 
