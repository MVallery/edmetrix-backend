from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from classes import services
from classes.models import ClassModel
router = APIRouter()

@router.post("/classes")
def create_class(data: dict= Body(...), db: Session = Depends(get_session)):
    return services.create_class(data, db)

@router.get("/classes/{user_id}")
def get_user_classes_route(user_id: int, db: Session = Depends(get_session)):
    return services.get_user_classes(user_id, db)

@router.get("/classes/{class_id}/students")
def get_class_students_route(class_id: int, db: Session = Depends(get_session)):
    return services.get_class_students(class_id, db)

@router.post("/classes/{class_id}/students")
def create_class_students_route(class_id: int, data: list[dict]= Body(...), db: Session = Depends(get_session)):
    return services.create_class_students(class_id, data, db)
