from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from classes.models import ClassModel, StudentClass
from classes.seating_charts.models import SeatingChart, StudentDesk

def save_student_desks(seating_chart_id: int, desks: list, db: Session):
  print('desks...', desks)
  db.add_all([
    StudentDesk(**{**desk, "seating_chart_id": seating_chart_id}) for desk in desks
  ])


def create_seating_chart(data: dict, db: Session):
  print('creating layout.....', data)
  # Save the overall layout
  new_chart = SeatingChart(**data['seating_chart'])
  db.add(new_chart)
  db.commit()
  db.refresh(new_chart)

  # Save the individual desks
  save_student_desks(new_chart.id, data['desks'], db)

  db.commit()

  return new_chart