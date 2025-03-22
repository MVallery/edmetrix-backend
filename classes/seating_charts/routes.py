from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from classes.seating_charts import services
from classes.seating_charts.models import Layout
router = APIRouter()

@router.post("/layout")
def create_layout_router(data: dict= Body(...), db: Session = Depends(get_session)):
    return services.create_layout(data, db)

@router.get("/layout/{teacher_id}")
def get_all_user_layout_router(teacher_id: int, db: Session = Depends(get_session)):
    return services.get_all_user_layout(teacher_id, db)

# @router.get("/layout/active")
# def get_active_layout_router(teacher_id: int, db: Session = Depends(get_session)):
#     return services.get_active_layout(teacher_id, db)

@router.get("/layout/{layout_id}")
def get_layout_router(layout_id: int, db: Session = Depends(get_session)):
    return services.get_layout(layout_id, db)

# @router.get("/layout/{layout_id}/desks")
# def get_layout_desks_router(layout_id: int, db: Session = Depends(get_session)):
#     return services.get_layout_desks(layout_id, db)

# @router.post("/layout/{layout_id}/desks")
# def create_layout_desks_router(layout_id: int, data: list[dict]= Body(...), db: Session = Depends(get_session)):
#     return services.create_layout_desks(layout_id, data, db)

