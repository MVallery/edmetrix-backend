from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
from ..base import Base

class User(Base):
  __tablename__ = "user"
  id = Column(Integer, primary_key=True, index=True)
  type = Column(Text(255)) # Teacher, Parent, Admin, Support
  name = Column(Text(255))
  img = Column(Text(255))
  email = Column(Text(255))
  password = Column(Text(255))
  premium = Column(Boolean)
  school = ForeignKey("school.id")
  # Notifications for student birthdays for teacher type = Student bdays
  bday_notification_day = Column(Text(255)) # day before, day of, both
  bday_notification_time = Column(Text(255)) # time 8:00AM

