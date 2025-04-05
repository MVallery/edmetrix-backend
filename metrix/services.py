from sqlalchemy.orm import Session, joinedload
from fastapi import Depends, Body
from classes.models import ClassModel, StudentClass
from _core.database import get_session
from metrix.models import Metric, ClassMetric

def create_class_metric(data, db: Session) -> dict:
  new_metric = ClassMetric(**data)
  db.add(new_metric)
  db.commit()
  db.refresh(new_metric)
  return new_metric

def create_metric(data, db: Session) -> dict:
  new_metric = Metric(**data)
  db.add(new_metric)
  db.commit()
  db.refresh(new_metric)

  # Save the individual class metrics
  for key, value in data['classes'].items():
    class_metric = ClassMetric(class_id = value.class_id, metric_id = new_metric.id)
    db.add(class_metric)
    db.commit()

  return new_metric


def get_metric(layout_id: int, db: Session):
  return db.query(Metric).options(joinedload(Metric.classes)).get(layout_id)

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