from auth.models.user import User
from auth.models.teacher import Teacher
from auth.models.userSchema import UserSchema
from sqlalchemy.orm import Session, joinedload, with_loader_criteria
from sqlalchemy import func

def create_teacher(user_id: str, db: Session):
    print('Creating teacher for user_id:', user_id)
    new_teacher = Teacher(user_id=user_id)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

# for now we will auto create a teacher when a user is created, and return the teacher_id within user, but
# in the future we may want to have a way to handle different user types
def create_user(data: dict, db: Session) -> UserSchema:
  print('Creating user with data:', data)
  new_user = User(**data)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  teacher = create_teacher(new_user.id, db)
  new_user.teacher = teacher
  return new_user

def get_user(user_id: str, db: Session) -> UserSchema:
  print('Fetching user with ID:', user_id)
  # user = db.query(User).filter(User.id == user_id).first()
  user = db.query(User).options(joinedload(User.teacher)).filter(User.id == user_id).first()
  if not user:
    raise ValueError(f"User with ID {user_id} not found")
  else:
    user.last_login = func.now()
    user.login_count = user.login_count + 1
    db.commit()
    db.refresh(user)
  return user

def update_user(user_id: str, data, db: Session) -> dict:
  print('Updating user with ID:', user_id)
  user = db.query(User).filter(User.id == user_id).first()
  allowed_fields = ['name', 'type']
  if not user:
    raise ValueError(f"User with ID {user_id} not found")
  
  for field in allowed_fields:
    if field in data:
      setattr(user, field, data[field])
  db.commit()
  db.refresh(user)
  return user