from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import relationship
from _models.base import Base

# To start off all users will be teachers, but keep it split bc eventually might have users that are
# parents, students, admins, support etc. For certain things we want to be able to specify teacher.

class TeacherContext(Base):
  __tablename__ = "teacher_context"
  id = Column(Integer, primary_key=True, index=True)

  teacher_id = Column(String(36), ForeignKey('teacher.id'))
  subject_id = Column(Integer, ForeignKey('subject.id'))
  category_name = Column(Text(255))


