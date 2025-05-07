from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from classes import class_services
from classes.models import ClassModel
router = APIRouter()

@router.post("/classes")
def create_class(data: dict= Body(...), db: Session = Depends(get_session)):
    return class_services.create_class(data, db)

@router.get("/classes/{teacher_id}")
def get_user_classes_route(teacher_id: int, db: Session = Depends(get_session)):
    return class_services.get_teacher_classes(teacher_id, db)
