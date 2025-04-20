from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from metrix.concept import subject_services
from metrix.concept.models import Concept
router = APIRouter()

# @router.post("/subjects")
# def create_subject(data: dict= Body(...), db: Session = Depends(get_session)):
#   return subject_services.create_subject(data, db)

# @router.put("/subjects/{subject_id}")
# def update_subject(subject_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
#   return subject_services.update_subject(subject_id, data, db)

# @router.get("/subjects/{subject_id}")
# def get_subjects(data: dict= Body(...), db: Session = Depends(get_session)):
#   return subject_services.get_subjects(data, db)
@router.get("/subjects")
def get_subjects(
  teacher_id: int | None = None,
  grade_level: str | None = None,

  db: Session = Depends(get_session),
):
  return subject_services.get_subjects(
    teacher_id=teacher_id,
    grade_level=grade_level,
    db=db,
  )


@router.delete("/subjects/{subject_id}")
def delete_subject(
  subject_id: int,
  db: Session = Depends(get_session),
):
  return subject_services.delete_metric(
    subject_id=subject_id,
    db=db,
  )

# @router.get("/subjects/class/{class_subject_id}")
# def get_class_subjects(data: dict= Body(...), db: Session = Depends(get_session)):
#   return subject_services.get_class_subjects(data, db)

@router.delete("/subjects/{subject_id}")
def delete_subject(
  subject_id: int,
  db: Session = Depends(get_session),
):
  return subject_services.delete_metric(
    subject_id=subject_id,
    db=db,
  )

@router.post("/subjects/class")
def create_class_subjects(data: dict= Body(...), db: Session = Depends(get_session)):
  return subject_services.create_class_subjects(data, db)

