from sqlalchemy.orm import Session, joinedload
from fastapi import Depends, Body
from classes.models import ClassModel, StudentClass
from _core.database import get_session
from metrix.models import Metric, ClassMetric, StudentMetric, Prep, ClassPrep
from fastapi import HTTPException

def create_class_metric(data, db: Session) -> dict:
  new_metric = ClassMetric(**data)
  db.add(new_metric)
  db.commit()
  db.refresh(new_metric)
  return new_metric

def create_metric(data, db: Session) -> dict:
  new_metric = Metric(**data.get('metric'))
  db.add(new_metric)
  db.commit()
  db.refresh(new_metric)

  # Save the individual class metrics for all similar preps (Same subject / grade_level)
  #### NEED TO ADD A JOIN HERE BC prep ID IS NOT IN TABLE, or change to
  #### grab prep_id and then on
  shared_preps = db.query(ClassPrep).filter(
    ClassPrep.prep_id == data['prep_id'],
    # ClassModel.grade_level == data['grade_level'],
  ).all()## save the class_id 
  print ('shared_preps', shared_preps)
  for key, value in shared_preps.items():
    print('key:value', key, value)
    class_metric = ClassMetric(class_id = value.class_id, metric_id = new_metric.id, date = data['date'])
    db.add(class_metric)
    db.commit()

  # pass in prep, then can use the grade_level, subject_id and teacher_id to find matching classes
  return new_metric

# def update_metric(subject_id: int, data: dict = Body(...), db: Session = Depends(get_session)):
#   return subject_services.update_subject(subject_id, data, db)

def update_metric(metric_id: int, data, db: Session):
  metric = db.query(Metric).get(metric_id)
  if not metric:
    raise HTTPException(status_code=404, detail="Metric not found")

  # Update layout fields
  for key, value in data.items():
    setattr(metric, key, value)
    

  db.commit()
  db.refresh(metric)

def get_metric(layout_id: int, db: Session):
  return db.query(Metric).options(joinedload(Metric.classes)).get(layout_id)

# CLASS METRICS
def get_class_metric(layout_id: int, db: Session):
  return db.query(ClassMetric).options(joinedload(Metric.desks)).get(layout_id)

def get_class_metrics(
  teacher_id: int | None = None,
  class_id: int | None = None,
  concept_id: int | None = None,
  start_date: str | None = None,
  end_date: str | None = None,
  db: Session = Depends(get_session),
) -> list:
  query = db.query(Metric)
  
  if teacher_id:
    query = query.filter(Metric.teacher_id == teacher_id)
  
  if class_id:
    query = query.filter(Metric.class_id == class_id)
  
  if concept_id:
    query = query.filter(Metric.concept_id == concept_id)
  
  if start_date:
    query = query.filter(Metric.date >= start_date)
  
  if end_date:
    query = query.filter(Metric.date <= end_date)
  
  return query.all()

def delete_metric(metric_id, db: Session):
  metric = db.query(Metric).get(metric_id)
  if metric:
    # First delete the associated ClassMetric records
    db.query(ClassMetric).filter(ClassMetric.metric_id == metric_id).delete(synchronize_session=False)
    # Then delete the Metric record itself
    db.delete(metric)
    db.commit()

  return metric

# STUDENT METRICS
def get_student_metric(student_metric_id: int, db: Session):
  return db.query(StudentMetric).get(student_metric_id)

def get_student_metrics(
  student_id: int | None = None,
  class_id: int | None = None,
  metric_id: int | None = None,
  concept_id: int | None = None,
  start_date: str | None = None,
  end_date: str | None = None,
  db: Session = Depends(get_session),
) -> list:
  query = db.query(StudentMetric)
  
  if student_id:
    query = query.filter(StudentMetric.student_id == student_id)
  
  if class_id:
    query = query.filter(StudentMetric.class_id == class_id)
  
  if concept_id:
    query = query.filter(StudentMetric.concept_id == concept_id)

  if metric_id:
    query = query.filter(StudentMetric.metric_id == metric_id)
  
  if start_date:
    query = query.filter(StudentMetric.date >= start_date)
  
  if end_date:
    query = query.filter(StudentMetric.date <= end_date)
  
  return query.all()

def create_student_metric(student_metric_id: int, data, db: Session) -> dict:
  new_student_metric = StudentMetric(**data)
  db.add(new_student_metric)
  db.commit()
  db.refresh(new_student_metric)
  return new_student_metric

def update_student_metric(student_metric_id: int, data, db: Session) -> dict:
  student_metric = db.query(StudentMetric).get(student_metric_id)
  if not student_metric:
    raise HTTPException(status_code=404, detail="Student Metric not found")
    
  db.commit()
  db.refresh(student_metric)
  return student_metric

def update_student_metrics(student_id: int, data, db: Session) -> dict:
  for student_metric in data.get('metrics', []):
    db.merge(StudentMetric(**student_metric))

  db.commit()

def create_student_metrics(student_id: int, data, db: Session) -> dict:
  for student_metric in data.get('metrics', []):
    new_student_metric = StudentMetric(**student_metric)
    db.add(new_student_metric)

  db.commit()

