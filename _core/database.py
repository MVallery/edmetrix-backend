from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from functools import wraps

DATABASE_URL = "mysql://root:rootpwd@localhost/edmetrix_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_session():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def db_transaction(func):
    @wraps(func)
    def wrapper(db: Session, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            db.commit()
            return result
        except:
            db.rollback()
            raise
    return wrapper
# # from app.core.database import SessionLocal

# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql://root:rootpwd@localhost/edmetrix_db"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#   db = SessionLocal()
#   try:
#     yield db
#   finally:
#     db.close()