from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from metrix.concept import concept_services
from metrix.concept.models import Concept
router = APIRouter()

@router.post("/concepts/")
def create_concept(data: dict= Body(...), db: Session = Depends(get_session)):
  return concept_services.create_concept(data, db)

@router.put("/concepts/{concept_id}")
def update_concept(concept_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
  return concept_services.update_concept(concept_id, data, db)

@router.get("/concepts/{concept_id}")
def get_concept(concept_id: int, db: Session = Depends(get_session)):
  return concept_services.get_concept(concept_id, db)


@router.get("/concepts")
def get_concepts(
  subject_id: int | None = None,
  parent_concept_id: int | None = None,
  is_main_concept: bool | None = None,
  is_global: bool | None = None,
  user_id: int | None = None,
  grade_level: str | None = None,

  db: Session = Depends(get_session),
):
  return concept_services.get_concepts(
    subject_id=subject_id,
    parent_concept_id=parent_concept_id,
    is_main_concept=is_main_concept,
    is_global=is_global,
    user_id=user_id,
    grade_level=grade_level,
    db=db,
  )
