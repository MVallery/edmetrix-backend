from sqlalchemy.orm import Session, joinedload
from classes.models import ClassModel, StudentClass
from metrix.concept.models import ClassSubject
from metrix.concept.subject_services import create_subject
from students.models import Student
from students.services import create_student

def create_class(data, db: Session) -> dict:
  subjects = data.pop("subjects", [])
  
  new_class = ClassModel(**data)
  db.add(new_class)
  db.commit()
  db.refresh(new_class)

  print(subjects, 'subjjjyyy')
  for subject in subjects:
    # remove items that are not needed in the class_subject table
    class_subject = {
      "class_id": new_class.id,
    }
    # if no subject id is preset it must be a newly created subject so create the main subject first
    if (not subject.get("subject_id")):
      main_subject_data = {'is_global': False, "name": subject.get("name"), 'teacher_id': new_class.teacher_id}
      main_subject = create_subject(main_subject_data, db)
      db.add(main_subject)
      db.commit()
      db.refresh(main_subject)
      class_subject["subject_id"] = main_subject.id

    # if a subject id is present, then it's an existing subject so just add the existing id
    else:
      class_subject["subject_id"] = subject["subject_id"]
    
    new_class_subject = ClassSubject(**class_subject)
    db.add(new_class_subject)
    db.commit()

  return new_class.id

def get_teacher_classes(teacher_id: int, db: Session):
  return db.query(ClassModel).options(joinedload(ClassModel.subjects)).filter(ClassModel.teacher_id == teacher_id).all()
