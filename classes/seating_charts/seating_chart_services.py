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

def desks_to_change(seating_chart_id, data, db):
  existing_desks = db.query(StudentDesk).filter(StudentDesk.seating_chart_id == seating_chart_id).all()
  incoming_desks = [{ "layout_desk_id": d["layout_desk_id"], "student_id": d["student_id"] } for d in data['desks']]

  # Build a set of (row, col) for easy comparison
  existing_set = {(d.layout_desk_id, d.student_id) for d in existing_desks}
  incoming_set = {(d["layout_desk_id"], d["student_id"]) for d in incoming_desks}

  # Delete removed desks
  to_delete = existing_set - incoming_set
  # Insert new desks
  to_create = incoming_set - existing_set

  return {'to_create': to_create, 'to_delete': to_delete}


def update_seating_chart(seating_chart_id: int, data, db: Session):
  seating_chart = db.query(SeatingChart).get(seating_chart_id)
  if not seating_chart:
    raise HTTPException(status_code=404, detail="Seating Chart not found")

  # Update layout fields
  for key, value in data['seating_chart'].items():
    setattr(seating_chart, key, value)
    
  desk_changes = desks_to_change(seating_chart_id, data, db)
  print('desk-changes', desk_changes)
  # delete old desks before adding new ones
  for layout_desk_id, _ in desk_changes['to_delete']:
    db.query(StudentDesk).filter(
        StudentDesk.seating_chart_id == seating_chart_id,
        StudentDesk.layout_desk_id == layout_desk_id,
    ).delete()

  # transform desks back to list[dict] for saving
  desks = [{"layout_desk_id": layout_desk_id, "student_id": student_id} for layout_desk_id, student_id in desk_changes['to_create']]
  save_student_desks(seating_chart_id, desks, db)

  db.commit()
  db.refresh(seating_chart)
  return get_seating_chart(seating_chart.id, db)

def get_seating_chart(seating_chart_id: int, db: Session):
  return db.query(SeatingChart).options(joinedload(SeatingChart.desks)).get(seating_chart_id)


# def get_all_class_seating_charts(class_id: int, db: Session):
#   seating_charts = db.query(SeatingChart).options(joinedload(SeatingChart.desks)).filter(SeatingChart.class_id == class_id,  SeatingChart.status != 'archived').order_by(SeatingChart.status.asc()).all()
#   return 

def get_active_seating_charts(teacher_id: int, db: Session):
  seating_charts = (
    db.query(SeatingChart)
    .join(SeatingChart.class_)  # join to access teacher_id
    .options(joinedload(SeatingChart.desks))  # eager load desks
    .filter(ClassModel.teacher_id == teacher_id, SeatingChart.status == 'active')
    .all()
)
  seating_charts_dict = {chart.class_id: chart for chart in seating_charts}

  return seating_charts_dict