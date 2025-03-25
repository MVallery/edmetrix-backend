from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from students import services
router = APIRouter()


@router.get("/students/class/{class_id}")
def get_class_students_route(class_id: int, db: Session = Depends(get_session)):
    return services.get_class_students(class_id, db)

@router.post("/students/class/{class_id}")
def create_class_students_route(class_id: int, data: list[dict]= Body(...), db: Session = Depends(get_session)):
    return services.create_class_students(class_id, data, db)
