from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from classes.models import ClassModel, StudentClass
from classes.seating_charts.models import Layout, LayoutDesk
# def create_layout(user_id: int, data, db: Session):
#   return db.query(ClassModel).filter(ClassModel.user_id == user_id).all()
def save_layout_desks(layout_id: int, desks: list, db: Session):
  print('desks...', desks)
  db.add_all([
    LayoutDesk(**{**desk, "layout_id": layout_id}) for desk in desks
  ])

def desks_to_change(layout_id, data, db):
  existing_desks = db.query(LayoutDesk).filter(LayoutDesk.layout_id == layout_id).all()
  incoming_desks = [{ "row": d["row"], "col": d["col"] } for d in data['desks']]

  # Build a set of (row, col) for easy comparison
  existing_set = {(d.row, d.col) for d in existing_desks}
  incoming_set = {(d["row"], d["col"]) for d in incoming_desks}

  # Delete removed desks
  to_delete = existing_set - incoming_set
  # Insert new desks
  to_create = incoming_set - existing_set

  return {'to_create': to_create, 'to_delete': to_delete}


def create_layout(data, db: Session) -> dict:
  print('creating layout.....', data)
  # Save the overall layout
  new_layout = Layout(**data['layout'])
  db.add(new_layout)
  db.commit()
  db.refresh(new_layout)

  # Save the individual desks
  save_layout_desks(new_layout.id, data['desks'], db)

  db.commit()

  return new_layout

def update_layout(layout_id: int, data, db: Session):
  layout = db.query(Layout).get(layout_id)
  if not layout:
    raise HTTPException(status_code=404, detail="Layout not found")

  # Update layout fields
  for key, value in data['layout'].items():
    setattr(layout, key, value)
    
  desk_changes = desks_to_change(layout_id, data, db)
  print('desk-changes', desk_changes)
  # delete old desks before adding new ones
  # db.query(LayoutDesk).filter(LayoutDesk.layout_id == layout_id).delete()
  for row, col in desk_changes['to_delete']:
    db.query(LayoutDesk).filter(
        LayoutDesk.layout_id == layout_id,
        LayoutDesk.row == row,
        LayoutDesk.col == col
    ).delete()

  # transform desks back to list[dict] for saving
  desks = [{"row": row, "col": col} for row, col in desk_changes['to_create']]
  save_layout_desks(layout_id, desks, db)

  db.commit()
  db.refresh(layout)
  return get_layout(layout.id, db)

def get_layout(layout_id: int, db: Session):
  return db.query(Layout).options(joinedload(Layout.desks)).get(layout_id)

# FUTURE: Add in archiveability and ability to get archived layouts
def get_all_teacher_layout(teacher_id: int, db: Session):
  return db.query(Layout).options(joinedload(Layout.desks)).filter(Layout.teacher_id == teacher_id,  Layout.status != 'archived').order_by(Layout.status.asc()).all()
# .order_by(
#     case(
#         (Layout.status == 'active', 0),
#         (Layout.status == 'inactive', 1)
#     )
# ) db.query(StudentClass).options(joinedload(StudentClass.student))

def create_layout_desk(data, db: Session):
  new_layout_desk = LayoutDesk(**data)
  db.add(new_layout_desk)
  db.commit()
  db.refresh(new_layout_desk)
  return new_layout_desk

def delete_layout_desk(desk_id, db: Session):
  desk = db.query(LayoutDesk).get(id)
  if desk:
    db.delete(desk)
    db.commit()
  return desk