
from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    type: str  # Teacher, Parent, Admin, Support
    name: str
    img: Optional[str] = Field(default=None)
    email: str
    password: str
    premium: Optional[bool] = Field(default=False)
    # school: Optional[int] = Field(default=None, foreign_key="school.id")
    bday_notification_day: Optional[str] = Field(default=None)  # day before, day of, both
    bday_notification_time: Optional[str] = Field(default=None)  # time like 8:00AM



# from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, JSON
# from ..base import Base

# class User(Base):
#   __tablename__ = "user"
#   id = Column(Integer, primary_key=True, index=True)
#   type = Column(Text(255)) # Teacher, Parent, Admin, Support
#   name = Column(Text(255))
#   img = Column(Text(255))
#   email = Column(Text(255))
#   password = Column(Text(255))
#   premium = Column(Boolean)
#   school = ForeignKey("school.id")
#   # Notifications for student birthdays for teacher type = Student bdays
#   bday_notification_day = Column(Text(255)) # day before, day of, both
#   bday_notification_time = Column(Text(255)) # time 8:00AM

