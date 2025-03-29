from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from students import services
from pydantic import BaseModel

router = APIRouter()
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    name: str

@router.get("/students/class/{class_id}")
def get_class_students_route(class_id: int, db: Session = Depends(get_session)):
    return services.get_class_students(class_id, db)

@router.post("/students/class/{class_id}")
def create_class_students_route(class_id: int, data: list[StudentCreate]= Body(...), db: Session = Depends(get_session)):
    print('creating class students route.....', data, class_id)
    return services.create_class_students(class_id, data, db)


# class_id 1
#  (NOBRIDGE) LOG  studentData [{"first_name": "Zoey", "last_name": "thebobi", "name": "Zoey thebobi"}]

# I get "Unprocessable entity"