from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from metrix.concept import subject_services
from metrix.concept.models import Concept
router = APIRouter()

@router.post("/subjects/")
def create_subject(data: dict= Body(...), db: Session = Depends(get_session)):
  return subject_services.create_subject(data, db)

# @router.put("/subjects/{subject_id}")
# def update_subject(subject_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
#   return subject_services.update_subject(subject_id, data, db)

@router.get("/subjects/{subject_id}")
def get_subjects(data: dict= Body(...), db: Session = Depends(get_session)):
  return subject_services.get_subjects(data, db)
