from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from auth import auth_services
router = APIRouter()

@router.post("/auth/user")
def create_class(data: dict= Body(...), db: Session = Depends(get_session)):
    return auth_services.create_user(data, db)

@router.get("/auth/user/{user_id}")
def get_user_route(user_id: int, db: Session = Depends(get_session)):
    return auth_services.get_user(user_id, db)

@router.put("/auth/user/{user_id}")
def update_user_route(user_id: int, db: Session = Depends(get_session)):
    return auth_services.update_user(user_id, db)
