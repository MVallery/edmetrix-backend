from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class AssignResult(Base):
    __tablename__ = "assign_result"
    id = Column(Integer, primary_key=True, index=True)
    assign_id = Column(Integer, ForeignKey('assign.id'))
    student_id = Column(Integer, ForeignKey('student.id'))
    score = Column(Integer)
    status = Column(Text(100)) # complete # incomplete # not_started # retest
    retest_score = Column(Integer)
    retest_status = Column(Text(100)) # complete # incomplete # not_started
