from sqlalchemy.orm import Session, joinedload
from classes.models import ClassModel, StudentClass
from students.models import Student
from students.services import create_student





def create_class(data, db: Session) -> dict:
  print('creating class.....', data)
  new_class = ClassModel(**data)
  print('after newclass')
  db.add(new_class)
  print('after add', new_class)
  db.commit()
  print('after commit')
  db.refresh(new_class)
  print('after refresh')
  return new_class

def get_teacher_classes(teacher_id: int, db: Session):
  return db.query(ClassModel).filter(ClassModel.teacher_id == teacher_id).all()
