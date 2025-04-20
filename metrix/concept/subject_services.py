from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, and_
from fastapi import Depends, Body
from classes.models import ClassModel, StudentClass
from _core.database import get_session
from metrix.concept.models import Subject, ClassSubject
from fastapi import HTTPException

def create_subject(data, db: Session) -> dict:
  new_subject = Subject(**data)
  db.add(new_subject)
  db.commit()
  db.refresh(new_subject)
  return new_subject

def get_subject(subject_id: int, db: Session):
  return db.query(Subject).get(subject_id)

# # CLASS METRICS
# def get_subject(layout_id: int, db: Session):
#   return db.query(Subject)


def get_subjects(
  teacher_id: int | None = None,
  grade_level: int | None = None,
  db: Session = Depends(get_session),
) -> list:
  query = db.query(Subject)

  #  for teacher specific subjects they might have created, these we will not filter by grade level
  # for global subjects, we will filter by grade level
  # query = query.filter( 
  #   # or_
  #                     #  (
  #   Subject.teacher_id == teacher_id,
  #   # and_(
  #   #   # Subject.is_global == True,
  #   #   Subject.grade_min <= grade_level,
  #   #   Subject.grade_max >= grade_level
  #   # )
  # # )
  # )
  results = query.all()
  print(f"Found {len(results)} subjects")
  for r in results:
      print(r.id, r.name, r.teacher_id, r.is_global, r.grade_min, r.grade_max)
  return results
  # return query.all()

def delete_subject(
  subject_id: int,
  db: Session = Depends(get_session),
):
  subject = db.query(Subject).get(subject_id)
  if not subject:
    raise HTTPException(status_code=404, detail="Subject not found")
  
  db.delete(subject)
  db.commit()
  return {"message": "Subject deleted successfully"}

## CLASS SUBJECTS


def create_class_subject(data, db: Session) -> dict:
  new_subject = ClassSubject(**data)
  db.add(new_subject)
  db.commit()
  db.refresh(new_subject)
  return new_subject

def create_class_subjects(data, db: Session) -> dict:
  new_subjects = [ClassSubject(**subject) for subject in data]
  db.add_all(new_subjects)
  db.commit()
  db.refresh(new_subjects)
  return new_subjects

def get_class_subject(subject_id: int, db: Session):
  return db.query(ClassSubject).get(subject_id)

# can just populate on the class model
# def get_class_subjects(class_id: int, db: Session):
#   return db.query(ClassSubject).filter(ClassSubject.class_id == class_id).all()

def delete_class_subject(
  subject_id: int,
  db: Session = Depends(get_session),
):
  subject = db.query(ClassSubject).get(subject_id)
  if not subject:
    raise HTTPException(status_code=404, detail="Class Subject not found")
  
  db.delete(subject)
  db.commit()
  return {"message": "Class Subject deleted successfully"}

# def get_class_subjects(
#   class_id: int,
#   db: Session,
# ) -> list:
#   query = db.query(ClassSubject)
#   if class_id:
#     query = query.filter(ClassSubject.class_id == class_id)
  
#   return query.all()