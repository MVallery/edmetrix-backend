from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from classes.seating_charts import layout_services
from classes.seating_charts import seating_chart_services
from classes.seating_charts.models import Layout
from classes.seating_charts.models.layout import LayoutSchema

router = APIRouter()

@router.post("/layout")
def create_layout_router(data: dict= Body(...), db: Session = Depends(get_session)):
    return layout_services.create_layout(data, db)

@router.get("/layout/{layout_id}")
def get_layout_router(layout_id: int, db: Session = Depends(get_session)):
    return layout_services.get_layout(layout_id, db)

@router.get("/layout/active/{teacher_id}", response_model=LayoutSchema)
def get_active_layout_router(teacher_id: int, db: Session = Depends(get_session)):
    return layout_services.get_active_layout(teacher_id, db)

@router.get("/layout")
def get_all_teacher_layout_router(teacher_id: int, db: Session = Depends(get_session)):
    return layout_services.get_all_teacher_layout(teacher_id, db)

@router.put("/layout/{layout_id}")
def update_layout_router(layout_id: int,data: dict= Body(...), db: Session = Depends(get_session)):
    return layout_services.update_layout(layout_id, data, db)



@router.post("/seating_chart")
def create_seating_chart_router(data: dict= Body(...), db: Session = Depends(get_session)):
    return seating_chart_services.create_seating_chart(data, db)


@router.get("/seating_chart/{seating_chart_id}")
def get_seating_chart_router(seating_chart_id: int, db: Session = Depends(get_session)):
    return seating_chart_services.get_seating_chart(seating_chart_id, db)

# @router.get("/seating_chart/class")
# def get_all_class_seating_charts_router(class_id: int, db: Session = Depends(get_session)):
#     return seating_chart_services.get_all_class_seating_charts(class_id, db)

@router.get("/seating_chart")
def get_all_class_seating_charts_router(teacher_id: int, db: Session = Depends(get_session)):
    return seating_chart_services.get_active_seating_charts(teacher_id, db)

@router.put("/seating_chart/{seating_chart_id}")
def update_seating_chart_router(seating_chart_id: int,data: dict= Body(...), db: Session = Depends(get_session)):
    return seating_chart_services.update_seating_chart(seating_chart_id, data, db)


# @router.get("/layout/active")
# def get_active_layout_router(teacher_id: int, db: Session = Depends(get_session)):
#     return services.get_active_layout(teacher_id, db)

# @router.get("/layout/{layout_id}/desks")
# def get_layout_desks_router(layout_id: int, db: Session = Depends(get_session)):
#     return services.get_layout_desks(layout_id, db)

# @router.post("/layout/{layout_id}/desks")
# def create_layout_desks_router(layout_id: int, data: list[dict]= Body(...), db: Session = Depends(get_session)):
#     return services.create_layout_desks(layout_id, data, db)

