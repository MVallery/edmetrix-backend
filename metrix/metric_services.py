from sqlalchemy.orm import Session, joinedload
from sqlalchemy.dialects.postgresql import insert

from fastapi import Depends, Body
from _core.database import get_session
from metrix.models import Metric, ClassMetric, StudentMetric, MasteryMetric, MasteryMetricHistory, Prep, ClassPrep
from fastapi import HTTPException
from collections import defaultdict

def create_mastery_metric(data, db: Session) -> dict:
  existing_mastery_metric = db.query(MasteryMetric).filter(
    MasteryMetric.student_id == data.get('student_id'),
    MasteryMetric.class_id == data.get('class_id'),
    MasteryMetric.concept_id == data.get('concept_id'),
  ).first()
  mastery_metric_id = 0
  existing_mastery_metric_level = 0


  # Update existing record
  if existing_mastery_metric:
    existing_mastery_metric_level = existing_mastery_metric.level
    existing_mastery_metric.level = data.get('level')
    mastery_metric_id = existing_mastery_metric.id
    db.commit()
    db.refresh(existing_mastery_metric)

  # Create new record & refresh to get id for history record later
  else:
    new_mastery_metric = MasteryMetric(
      student_id=data.get('student_id'),
      class_id=data.get('class_id'),
      concept_id=data.get('concept_id'),
      level=data.get('level'),
    )
    db.add(new_mastery_metric)
    db.commit()
    db.refresh(new_mastery_metric)
    mastery_metric_id = new_mastery_metric.id

  # If there's a change in level, create a history record
  old_level = existing_mastery_metric_level if existing_mastery_metric else None
  new_level = data.get('level')
  if old_level != new_level:
    metric_history = MasteryMetricHistory(
      mastery_metric_id=mastery_metric_id,
      old_level =  existing_mastery_metric_level if existing_mastery_metric else None,
      new_level = data.get('level'),
      class_id=data.get('class_id'),
    )

    db.add(metric_history)
    db.commit()

def create_mastery_metrics(data, db: Session) -> dict:
  for student_id in data.get('selected_student_ids', []):
    data['student_id'] = student_id
    create_mastery_metric(data, db)


def get_mastery_metrics(
  student_id: int | None = None,
  class_id: int | None = None,
  concept_id: int | None = None,
  db: Session = Depends(get_session),
) -> list:
  query = db.query(MasteryMetric)
  
  if student_id:
    query = query.filter(MasteryMetric.student_id == student_id)
  
  if class_id:
    query = query.filter(MasteryMetric.class_id == class_id)

  if concept_id:
    query = query.filter(MasteryMetric.concept_id == concept_id)

  result = defaultdict(dict)
  for mastery_metric in query.all():
    result[mastery_metric.student_id] = {
      "level": mastery_metric.level,
      "notes": mastery_metric.notes
    }
    result['concept_id'] = concept_id
    print('result', dict(result))
  return dict(result)
  # tweak this to return object {[student_id: metric level]} **********************************************
  # return query.all()
  #  stmt = insert(MasteryMetric).values(
  #     student_id=student_id,
  #     class_id=data['class_id'],
  #     concept_id=data['concept_id'],
  #     level=data['level'],
  #   )
  #   stmt = stmt.on_conflict_do_update(
  #     index_elements=['student_id', 'concept_id'],
  #     set_={'class_id': stmt.excluded.class_id}
  #   )
  #   db.execute(stmt)







#### NOT USED FOR MVP
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

# def update_metric(metric_id: int, data, db: Session):
#   metric = db.query(Metric).get(metric_id)
#   if not metric:
#     raise HTTPException(status_code=404, detail="Metric not found")

#   # Update layout fields
#   for key, value in data.items():
#     setattr(metric, key, value)
    

#   db.commit()
#   db.refresh(metric)

# def get_metric(layout_id: int, db: Session):
#   return db.query(Metric).options(joinedload(Metric.classes)).get(layout_id)

# CLASS METRICS
# def get_class_metric(layout_id: int, db: Session):
#   return db.query(ClassMetric).options(joinedload(Metric.desks)).get(layout_id)

# def get_class_metrics(
#   teacher_id: int | None = None,
#   class_id: int | None = None,
#   prep_concept_id: int | None = None,
#   start_date: str | None = None,
#   end_date: str | None = None,
#   db: Session = Depends(get_session),
# ) -> list:
#   query = db.query(Metric)
  
#   if teacher_id:
#     query = query.filter(Metric.teacher_id == teacher_id)
  
#   if class_id:
  
#   if prep_concept_id:
#     query = query.filter(Metric.prep_concept_id == prep_concept_id)
  
#   if start_date:
#     query = query.filter(Metric.date >= start_date)
  
#   if end_date:
#     query = query.filter(Metric.date <= end_date)
  
#   return query.all()

# def delete_metric(metric_id, db: Session):
#   metric = db.query(Metric).get(metric_id)
#   if metric:
#     # First delete the associated ClassMetric records
#     db.query(ClassMetric).filter(ClassMetric.metric_id == metric_id).delete(synchronize_session=False)
#     # Then delete the Metric record itself
#     db.delete(metric)
#     db.commit()

#   return metric

# # STUDENT METRICS
# def get_student_metric(student_metric_id: int, db: Session):
#   return db.query(StudentMetric).get(student_metric_id)

# def get_student_metrics(
#   student_id: int | None = None,
#   class_id: int | None = None,
#   metric_id: int | None = None,
#   concept_id: int | None = None,
#   start_date: str | None = None,
#   end_date: str | None = None,
#   db: Session = Depends(get_session),
# ) -> list:
#   query = db.query(StudentMetric)
  
#   if student_id:
#     query = query.filter(StudentMetric.student_id == student_id)
  
#   if class_id:
#     query = query.filter(StudentMetric.class_id == class_id)
  
#   if concept_id:
#     query = query.filter(StudentMetric.concept_id == concept_id)

#   if metric_id:
#     query = query.filter(StudentMetric.metric_id == metric_id)
  
#   if start_date:
#     query = query.filter(StudentMetric.date >= start_date)
  
#   if end_date:
#     query = query.filter(StudentMetric.date <= end_date)
  
#   return query.all()

# def create_student_metric(student_metric_id: int, data, db: Session) -> dict:
#   new_student_metric = StudentMetric(**data)
#   db.add(new_student_metric)
#   db.commit()
#   db.refresh(new_student_metric)
#   return new_student_metric

# def update_student_metric(student_metric_id: int, data, db: Session) -> dict:
#   student_metric = db.query(StudentMetric).get(student_metric_id)
#   if not student_metric:
#     raise HTTPException(status_code=404, detail="Student Metric not found")
    
#   db.commit()
#   db.refresh(student_metric)
#   return student_metric

# def update_student_metrics(student_id: int, data, db: Session) -> dict:
#   for student_metric in data.get('metrics', []):
#     db.merge(StudentMetric(**student_metric))

#   db.commit()

# def create_student_metrics(student_id: int, data, db: Session) -> dict:
#   for student_metric in data.get('metrics', []):
#     new_student_metric = StudentMetric(**student_metric)
#     db.add(new_student_metric)

#   db.commit()

