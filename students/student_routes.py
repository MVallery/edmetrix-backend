from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from students import student_services
from pydantic import BaseModel

router = APIRouter()
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    name: str
    email: str | None = None
    birthday: str | None = None
    img: str | None = None
    grade_level: int | None = None
    school_student_id: str | None = None  # ID used by the school system, if applicable
    school_id: int | None = None
    gender: str | None = None  # M, F, O

class StudentOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    name: str
    email: str | None = None
    birthday: str | None = None
    img: str | None = None
    grade_level: int | None = None
    active: bool = True

class StudentClassOut(BaseModel):
    student_id: int
    class_id: int
    active: bool

@router.get("/students/class/{class_id}")
def get_class_students_route(class_id: int, db: Session = Depends(get_session)):
    return student_services.get_class_students(class_id, db)

@router.post("/students/class/{class_id}")
def create_class_students_route(class_id: int, data: list[StudentCreate]= Body(...), db: Session = Depends(get_session)):
    print('creating class students route.....', data, class_id)
    return student_services.create_class_students(class_id, data, db)

@router.put("/students/class/{id}", response_model=StudentClassOut)
def update_class_student_route(id: int, data = Body(...), db: Session = Depends(get_session)):
    print('updating class students route.....', data, id)
    return student_services.update_class_student(id, data, db)

@router.put("/students/{id}", response_model=StudentOut)
def update_student_route(id: int, data: dict = Body(...), db: Session = Depends(get_session)):
    print('updating student route.....', data, id)
    return student_services.update_student(id, data, db)
# class_id 1
#  (NOBRIDGE) LOG  studentData [{"first_name": "Zoey", "last_name": "thebobi", "name": "Zoey thebobi"}]

# I get "Unprocessable entity"