from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class QuestionResponse(Base):
    __tablename__ = "question_response"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    student_id = Column(Integer, ForeignKey('student.id'))
    mistake_id = Column(Integer, ForeignKey('mistake.id'))
    text = Column(Text(255))