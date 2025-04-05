
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from .models import Subject

# def get_subjects(data, db: Session):
#   return db.query(Subject).filter(
#     user_id=data.user_id if data.user_id,
#     is_
#       ).get(layout_id)
