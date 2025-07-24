from sqlalchemy.orm import Session, joinedload, with_loader_criteria
from classes.models import ClassModel
from metrix.concept.models import PrepConcept, Prep, ClassPrep
from metrix.concept.subject_services import create_subject
from students.student_services import create_student

# each grade level / subject combo will be considered one "prep", 
# teachers can have multiple subjects so they can have multiple preps
# for now teachers can only specify one grade level, but eventually we will allow multiple grade levels

def create_preps(subjects, new_class, db: Session):
  for subject in subjects:
    print('Creating subject for class:', subject)
    # first see if we already have the same prep for this subject and grade level
    prep = db.query(Prep).filter(
      Prep.subject_id == subject,
      Prep.grade_level == new_class.grade_level,
      Prep.teacher_id == new_class.teacher_id
    ).first()

    # if we do not already have this prep grade level / subject combo in the preps table, then create a new one.
    if not prep:
      prep = Prep(
        subject_id=subject,
        teacher_id=new_class.teacher_id,
        grade_level=new_class.grade_level,
      )
      db.add(prep)
      db.commit()
      db.refresh(prep)

    # Create a new class_prep join table for each prep
    class_prep = ClassPrep(
      class_id=new_class.id,
      prep_id=prep.id,
    )
    db.add(class_prep)
    db.commit()
    db.refresh(class_prep)

def update_class(class_id: int, data: dict, db: Session) -> dict:
  print('Updating class with ID:', class_id)
  class_model = db.query(ClassModel).get(class_id)
  if not class_model:
    raise ValueError(f"Class with ID {class_id} not found")

  # Update class fields
  for key, value in data.items():
    setattr(class_model, key, value)

  db.commit()
  db.refresh(class_model)
  
  return class_model
  


def create_class(data, db: Session) -> dict:
  print('Creating class with data:', data)
  subjects = data.pop("subjects", [])
  new_class = ClassModel(**data)
  db.add(new_class)
  db.commit()
  db.refresh(new_class)
  create_preps(subjects, new_class, db)

  print(subjects, 'subjjjyyy')
 
  return new_class.id
# def get_teacher_classes(teacher_id: int, db: Session):
#   return db.query(ClassModel).options(
#     joinedload(ClassModel.subjects)
#         .joinedload(Prep.subject),
#     joinedload(ClassModel.subjects)
#         .joinedload(Prep.concepts)
#         .joinedload(PrepConcept.concept),      
#     with_loader_criteria(PrepConcept, PrepConcept.active == True)
#     ).filter(ClassModel.teacher_id == teacher_id).all()

def get_teacher_classes(teacher_id: int, db: Session):
  return db.query(ClassModel).options(
  # joinedload(ClassModel.preps)
  #   .joinedload(ClassPrep.prep)
  #     .joinedload(Prep.concepts)
  #       .joinedload(PrepConcept.concept),
  joinedload(ClassModel.preps)
    .joinedload(ClassPrep.prep)
      .joinedload(Prep.subject),
  joinedload(ClassModel.preps)
    .joinedload(ClassPrep.prep)
      .joinedload(Prep.concepts)
        .joinedload(PrepConcept.concept),
  with_loader_criteria(PrepConcept, PrepConcept.active == True)
).filter(ClassModel.teacher_id == teacher_id).all()
  # return db.query(ClassModel).options(
  #   joinedload(ClassModel.preps)
  #     .joinedload(ClassPrep.prep)
  #       .joinedload(Prep.concepts)
  #       .joinedload(Prep.subject),
  #   with_loader_criteria(PrepConcept, PrepConcept.active == True)
  # ).filter(ClassModel.teacher_id == teacher_id).all()




# def get_teacher_classes(teacher_id: int, db: Session):
#   return db.query(ClassModel).options(
#     # joinedload(ClassModel.preps)
#     joinedload(ClassModel.preps)
#       .joinedload(ClassPrep.prep)
#         .joinedload(Prep.concepts)
#           .joinedload(PrepConcept.concept),  
#       joinedload(ClassModel.preps) 
#         .joinedload(ClassPrep.prep)
#           .joinedload(Prep.subject),
#     with_loader_criteria(PrepConcept, PrepConcept.active == True)
#     ).filter(ClassModel.teacher_id == teacher_id).all()
