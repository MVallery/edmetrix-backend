from students.models import Student
from sqlalchemy.orm import Session, joinedload
from students.models import Student, StudentClass
from classes.seating_charts.seating_chart_services import delete_student_desk
def create_student(data, db: Session):
  new_student = Student(**data.dict()) # use when you set a Pydantic model like StudentCreate, you must unpack the data
  db.add(new_student)
  db.flush()
  return new_student


def get_class_students(class_id: any, db: Session):
  print('getting class students.....', class_id)
  # results = (
  #   db.query(StudentClass, Student)
  #   .join(Student, StudentClass.student_id == Student.id)
  #   .filter(StudentClass.class_id == class_id)
  #   .all()
  # )
  return db.query(StudentClass).options(joinedload(StudentClass.student)).filter(StudentClass.class_id == class_id, StudentClass.active == True).all()

# db.query(StudentClass).filter(StudentClass.class_id == class_id).all()

def create_class_students(class_id: any, data, db: Session):
  print('creating class students.....', data)
  for student in data:
    class_student = {"class_id": class_id}
    # this is a new student that hasn't been generated yet, so create a base Student that can be shared amongst teachers / added to a school.
    if 'id' not in student:
      new_student = create_student(student, db)
      # new_student = Student(**student)
      # db.add(new_student)
      # db.flush()
      class_student['student_id'] = new_student.id  # inject newly created student id into the class student
    else:
      class_student['student_id'] = student['id']
    # Create the student / class JOIN table
    # student['class_id'] = class_id
    db.add(StudentClass(**class_student))
  db.commit()
  return True

  # db.add_all([StudentClass(**student) for student in data])

# db.add_

def update_class_student(id, data, db: Session):
  print('updating class students.....', data)
  # Delete all existing students in this class
  allowed_fields = ['active']
  student = db.query(StudentClass).filter(StudentClass.id == id).first()
  if student:
    for field in allowed_fields:
      if field in data:
        setattr(student, field, data[field])
      if field == 'active':
        delete_student_desk(student.id, db)

    db.commit()
  db.commit()

  return student


def update_student(student_id: int, data, db: Session):
  print('updating student.....', data)
  student = db.query(Student).filter(Student.id == student_id).first()
  allowed_fields = ['first_name', 'last_name', 'name']
  if not student:
    return None
  for field in allowed_fields:
    if field in data:
      setattr(student, field, data[field])
  db.commit()
  print('updated student:', student)
  return student
  