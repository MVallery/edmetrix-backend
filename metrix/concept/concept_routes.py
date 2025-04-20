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
  user_id: int | None = None,
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
class SharedConceptUpdate(BaseModel):
    id: int
    concept_id: int
    shared_subject_id: int
    active: bool

class UpdateSharedConceptsRequest(BaseModel):
    concepts: List[SharedConceptUpdate]
    teacher_id: int


@router.post("/concepts/shared")
def create_shared_concepts(data: dict = Body(...), db: Session = Depends(get_session)):
  return concept_services.create_shared_concepts(data, db)

@router.post("/concepts/shared/update")
def update_shared_concepts(data: UpdateSharedConceptsRequest, db: Session = Depends(get_session)):
  print('updating shared concepts.....', data)
  return concept_services.update_shared_concepts(data, db)

@router.put("/concepts/shared/{concept_id}")
def update_concept(concept_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
  return concept_services.update_concept(concept_id, data, db)

# @router.get("/concepts/shared/{concept_id}")
# def get_concept(concept_id: int, db: Session = Depends(get_session)):
#   return concept_services.get_concept(concept_id, db)

