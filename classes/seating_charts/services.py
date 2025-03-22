from sqlalchemy.orm import Session, joinedload
from classes.models import ClassModel, StudentClass
from classes.seating_charts.models import Layout, LayoutDesk
# def create_layout(user_id: int, data, db: Session):
#   return db.query(ClassModel).filter(ClassModel.user_id == user_id).all()

def create_layout(data, db: Session) -> dict:
  print('creating layout.....', data)
  # Save the overall layout
  new_layout = Layout(**data['layout'])
  db.add(new_layout)
  db.commit()
  db.refresh(new_layout)

  # Save the individual desks
  db.add_all([LayoutDesk(**layout) for layout in data['desks']])
  db.commit()

  return new_layout

def get_layout(layout_id: int, db: Session):
  return db.query(Layout).options(joinedload(LayoutDesk.desks)).get(layout_id)

# FUTURE: Add in archiveability and ability to get archived layouts
def get_all_user_layout(user_id: int, db: Session):
  return db.query(Layout).options(joinedload(LayoutDesk.desks)).filter(Layout.teacher_id == user_id,  Layout.status != 'archived').order_by(Layout.status.desc()).all()
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