from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from ..base import Base

class Question_Response(Base):
    __tablename__ = "question_response"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(ForeignKey('question.id'))
    student_id = Column(ForeignKey('student.id'))
    mistake_id = Column(ForeignKey('mistake.id'))
    text = Column(Text(255))
