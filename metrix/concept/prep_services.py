from sqlalchemy.orm import Session, joinedload, with_loader_criteria
from sqlalchemy import or_, and_
from fastapi import Depends, Body
from _core.database import get_session
from metrix.concept.models import PrepConcept, Concept, Prep, ClassPrep

def get_class_preps(class_id: int, db: Session):
  return db.query(ClassPrep).options(
    joinedload(ClassPrep.prep)
      .joinedload(Prep.concepts)
        .joinedload(PrepConcept.concept),
    joinedload(ClassPrep.prep)
      .joinedload(Prep.subject),
    # with_loader_criteria(PrepConcept, 
    #                     #  PrepConcept.active == True
    #                      )
    ).filter((ClassPrep.class_id == class_id)).all()

def get_teacher_preps(teacher_id: int, db: Session):
  return db.query(Prep).options(
    # joinedload(Prep.concepts),
      # .joinedload(PrepConcept.concept),
    joinedload(Prep.subject)
  ).filter((ClassPrep.teacher_id == teacher_id)).all()
