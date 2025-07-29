from pydantic import BaseModel

class TeacherSchema(BaseModel):
    id: int
    user_id: str
    # add any other fields you want from Teacher

    class Config:
        orm_mode = True