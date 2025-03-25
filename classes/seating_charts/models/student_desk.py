from sqlalchemy import Column, Integer, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from typing import Optional
from _models.base import Base

class StudentDesk(Base):
  __tablename__ = "student_desk"

  id = Column(Integer, primary_key=True, index=True)
  layout_desk_id = Column(ForeignKey("layout_desk.id"))
  seating_chart_id = Column(ForeignKey("seating_chart.id"))
  student_id = Column(ForeignKey("student.id"))

  position = relationship("LayoutDesk")

