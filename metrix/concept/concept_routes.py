from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from _core.database import get_session
from metrix.concept import concept_services
from metrix.concept.models import Concept
router = APIRouter()
from pydantic import BaseModel
from typing import List

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
  user_id: str | None = None,
  parent_concept_id: int | None = None,
  is_main_concept: bool | None = None,
  is_global: bool | None = None,
  grade_level: str | None = None,

  db: Session = Depends(get_session),
):
  print('getting concepts routes', )
  return concept_services.get_concepts(
    subject_id=subject_id,
    user_id=user_id,
    parent_concept_id=parent_concept_id,
    is_main_concept=is_main_concept,
    is_global=is_global,
    grade_level=grade_level,
    db=db,
  )
class PrepConceptUpdate(BaseModel):
    id: int
    concept_id: int
    prep_id: int
    active: bool

class UpdatePrepConceptsRequest(BaseModel):
    concepts: List[PrepConceptUpdate]
    teacher_id: int


@router.post("/concepts/prep")
def create_prep_concepts(data: dict = Body(...), db: Session = Depends(get_session)):
  return concept_services.create_prep_concepts(data, db)

@router.post("/concepts/prep/update")
def update_prep_concepts(data: UpdatePrepConceptsRequest, db: Session = Depends(get_session)):
  print('updating prep concepts.....', data)
  return concept_services.update_prep_concepts(data, db)

@router.put("/concepts/prep/{concept_id}")
def update_concept(concept_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
  return concept_services.update_concept(concept_id, data, db)

# @router.get("/concepts/prep/{concept_id}")
# def get_concept(concept_id: int, db: Session = Depends(get_session)):
#   return concept_services.get_concept(concept_id, db)

