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
