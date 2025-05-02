from sqlalchemy.orm import Session, joinedload, with_loader_criteria
from classes.models import ClassModel, StudentClass
from metrix.concept.models import ClassSubject, PrepConcept, Prep
from metrix.concept.subject_services import create_subject
from students.models import Student
from students.services import create_student

def create_subjects(subjects, new_class, db: Session):
   for subject in subjects:
    prep = db.query(Prep).filter(
      Prep.subject_id == subject.get("subject_id"),
      Prep.grade_level == subject.get("grade_level"),
      Prep.teacher_id == new_class.teacher_id
    ).first()

    # if we do not already have this grade level / subject combo in the preps table, then create a new one.
    if not prep:
      new_prep = Prep(
        subject_id=subject.get("subject_id"),
        teacher_id=new_class.teacher_id,
        grade_level=new_class.grade_level,
      )
      db.add(new_prep)
      db.commit()
      db.refresh(new_prep)

def create_class(data, db: Session) -> dict:
  subjects = data.pop("subjects", [])
  new_class = ClassModel(**data)
  create_subjects(subjects, new_class, db)
  db.add(new_class)
  db.commit()
  db.refresh(new_class)

  print(subjects, 'subjjjyyy')
 
  return new_class.id

def get_teacher_classes(teacher_id: int, db: Session):
  return db.query(ClassModel).options(
    joinedload(ClassModel.subjects)
        .joinedload(Prep.subject),
    joinedload(ClassModel.subjects)
        .joinedload(Prep.concepts)
        .joinedload(PrepConcept.concept),      
    with_loader_criteria(PrepConcept, PrepConcept.active == True)
    ).filter(ClassModel.teacher_id == teacher_id).all()
