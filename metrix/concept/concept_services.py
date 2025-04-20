from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, and_
from fastapi import Depends, Body
from _core.database import get_session
from metrix.concept.models import SharedConcept, Concept, SharedSubject

def create_shared_concept(data, db: Session) -> dict:
  new_shared_concept = SharedConcept(
  concept_id=data.get("concept_id"),
  shared_subject_id=data.get("shared_subject_id"),
  )
  db.add(new_shared_concept)
  db.commit()
  db.refresh(new_shared_concept)

def update_shared_concept(data, db: Session) -> dict:
    print('updating shared concept.....', data, data.get("shared_subject_id"))
    shared_concept = db.query(SharedConcept).filter(
      SharedConcept.concept_id == data.get("concept_id"),
      SharedConcept.shared_subject_id == data.get("shared_subject_id")
    ).first()

    if not shared_concept:
      create_shared_concept(data, db)
    else:
      shared_concept.active = data.get("active")
      db.commit()
      db.refresh(shared_concept)


def update_shared_concepts(data, db: Session) -> dict:
  print('updating shared concepts.....', data)
  for concept in data.concepts:
    shared_concept_data = {
      "concept_id": concept.concept_id,
      "shared_subject_id": concept.shared_subject_id,
      "active": concept.active,
    }
    update_shared_concept(shared_concept_data, db)
    return db.query(SharedConcept).join(SharedConcept.shared_subject).options(
      joinedload(SharedConcept.concept)
    ).filter(
      SharedConcept.shared_subject.has(SharedSubject.teacher_id == data.teacher_id),
      SharedConcept.active == True
    ).all()


def create_shared_concepts(data, db: Session) -> dict:
  print('updating shared concepts.....', data)
  for concept in data.get("concepts"):
    shared_concept_data = {
      "concept_id": concept.get("concept_id"),
      "shared_subject_id": concept.get("shared_subject_id"),
      "active": concept.get("active"),
    }

    # if this is a newly created concept, then create a new base concept & set that concept_id
    if concept.get("concept_id") is None:
      concept_data = {
        "name": concept.get("name"),
        "is_global": False,
        "is_main_concept": False,
        "grade_level": concept.get("grade_level"),
        "subject_id": concept.get("subject_id"),
        "user_id": concept.get("user_id"),
      }
      new_concept = create_concept(concept_data, db)
      shared_concept_data["concept_id"] = new_concept.id  # inject newly created concept id into the shared concept

    update_shared_concept(shared_concept_data, db)

  # return an updated list of all the shared concepts for this subject
  return db.query(SharedConcept).options(
      joinedload(SharedConcept.concept)
    ).filter(
    SharedConcept.shared_subject_id == data.get("concepts")[0].get("shared_subject_id"),
    SharedConcept.active == True
  ).all()

def create_concept(data, db: Session):
  new_concept = Concept(**data.dict()) # use when you set a Pydantic model like StudentCreate, you must unpack the data
  db.add(new_concept)
  db.flush()
  return new_concept

def get_concepts(
  subject_id: int | None = None,
  user_id: int | None = None,
  parent_concept_id: int | None = None,
  is_main_concept: bool | None = None,
  is_global: bool | None = True,
  grade_level: str | None = None,
  db: Session = Depends(get_session),
) -> list:
  query = db.query(Concept)
  print('getting concepts.....', subject_id, user_id, parent_concept_id, is_main_concept, is_global, grade_level)
  if subject_id:
    query = query.filter(Concept.subject_id == subject_id)
  
  if user_id:
    query = query.filter(
       or_(
        Concept.user_id == user_id,
        Concept.is_global == True
      )
    )
  
  if parent_concept_id:
    query = query.filter(Concept.parent_concept_id == parent_concept_id)
  
  if is_main_concept:
    query = query.filter(Concept.is_main_concept == is_main_concept)
  
  if grade_level:
    query = query.filter(Concept.grade_min <= grade_level, Concept.grade_max >= grade_level)

  return query.all()
