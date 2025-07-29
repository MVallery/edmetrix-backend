from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from auth.models.teacherSchema import TeacherSchema

class UserSchema(BaseModel):
    id: str
    type: Optional[str]
    name: Optional[str]
    img: Optional[str]
    email: str
    premium: Optional[bool]
    school_id: Optional[int]
    bday_notification_day: Optional[str]
    bday_notification_time: Optional[str]
    signup_date: datetime
    last_login: Optional[datetime]
    login_count: int
    # settings: Optional[dict]
    teacher: Optional[TeacherSchema]  # include manually if needed

    class Config:
        orm_mode = True