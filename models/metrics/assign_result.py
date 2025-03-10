from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Assign_Result(Base):
    __tablename__ = "assign_result"
    id = Column(Integer, primary_key=True, index=True)
    assign_id = Column(ForeignKey('assign.id'))
    student_id = Column(ForeignKey('student.id'))
    score = Column(Integer)
    status = Column(Text(100)) # complete # incomplete # not_started # retest
    retest_score = Column(Integer)
    retest_status = Column(Text(100)) # complete # incomplete # not_started


