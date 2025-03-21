from sqlalchemy.orm import Session
from classes.models import ClassModel, StudentClass
from students.models import Student

def create_student(data, db: Session):
  new_student = Student(**data)
  db.add(new_student)
  db.flush()
  return new_student

  # db.add_