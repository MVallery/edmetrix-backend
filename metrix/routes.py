from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from metrix import services
from metrix.models import Metric
router = APIRouter()

@router.post("/metrics/")
def create_metric(data: dict= Body(...), db: Session = Depends(get_session)):
  return services.create_metric(data, db)

@router.put("/metrics/{metric_id}")
def update_metric(metric_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
  return services.update_metric(metric_id, data, db)

@router.get("/metrics/{metric_id}")
def get_metric(metric_id: int, db: Session = Depends(get_session)):
  return services.get_metric(metric_id, db)


@router.get("/metrics")
def get_metrics(
  teacher_id: int | None = None,
  class_id: int | None = None,
  concept_id: int | None = None,
  start_date: str | None = None,
  end_date: str | None = None,
  db: Session = Depends(get_session),
):
  return services.get_metrics(
    teacher_id=teacher_id,
    class_id=class_id,
    concept_id=concept_id,
    start_date=start_date,
    end_date=end_date,
    db=db,
  )

@router.get("/metrics/students/{student_metric_id}")
def get_student_metric(student_metric_id: int, db: Session = Depends(get_session)):
  return services.get_student_metric(student_metric_id, db)


@router.post("/metrics/students/{student_metric_id}")
def create_student_metric(student_metric_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
  return services.create_student_metric(student_metric_id, data, db)

@router.put("/metrics/students/{student_metric_id}")
def update_student_metric(student_metric_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
  return services.update_student_metric(student_metric_id, data, db)

@router.get("/metrics/students")
def get_student_metrics(
  student_id: int | None = None, # pull all metrics for a student (For student page)
  class_id: int | None = None, #pull all metrics for a class (For dashboard)
  concept_id: int | None = None, # pull all metrics for a concept (For dashboard)
  metric_id: int | None = None, # pull all student metrics for a metric_id, viewing student results
  date: str | None = None, # pull all student metrics for a date, viewing student results/dashboard
  db: Session = Depends(get_session),
):
  return services.get_student_metrics(
    student_id=student_id,
    class_id=class_id,
    metric_id=metric_id,
    concept_id=concept_id,
    date=date,
    db=db,
  )

@router.delete("/metrics")
def delete_metric(
  metric_id: int,
  class_metric_id: int,
  db: Session = Depends(get_session),
):
  return services.delete_metric(
    metric_id=metric_id,
    class_metric_id=class_metric_id,
    db=db,
  )