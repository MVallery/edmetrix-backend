from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import relationship
from _models.base import Base

# To start off all users will be teachers, but keep it split bc eventually might have users that are
# parents, students, admins, support etc. For certain things we want to be able to specify teacher.

# user_id and teacher_id are the same
class Teacher(Base):
  __tablename__ = "teacher"
  id = Column(Integer, primary_key=True, index=True)
  type = Column(Text(255), default='Teacher') # Teacher, SPED Teacher, Intervention Specialist, Home School Teacher,



  user_id = Column(String(36), ForeignKey('user.id'))
  user = relationship("User", back_populates="teacher")



