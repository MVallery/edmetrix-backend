from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from metrix.concept import prep_services
from metrix.concept.models import Concept
router = APIRouter()
from pydantic import BaseModel
from typing import List

@router.post("/prep/")
def update_prep(data: dict= Body(...), db: Session = Depends(get_session)):
  return prep_services.update_prep(data, db)

@router.get("/prep/class/{class_id}")
def get_class_preps(class_id: int, db: Session = Depends(get_session)):
  return prep_services.get_class_preps(class_id, db)

@router.get("/prep/teacher/{teacher_id}")
def get_teacher_preps(teacher_id: int, db: Session = Depends(get_session)):
  return prep_services.get_teacher_preps(teacher_id, db)
