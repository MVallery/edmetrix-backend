
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, create_engine, Session
from models.class_models.class_model import Class_Model
from fastapi import Request

DATABASE_URL = "mysql://root:rootpwd@localhost/edmetrix_db"
engine = create_engine(DATABASE_URL)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/classes/")
def create_class(data: Class_Model):
    print('creating class.....')
    with Session(engine) as session:
        new_class = Class_Model(**data.model_dump())
        session.add(new_class)
        session.commit()
        session.refresh(new_class)
        return new_class



@app.post("/test/")
def just_test(data: Class_Model):
    print('creating class.....')
    with Session(engine) as session:
        new_class = Class_Model(**data.model_dump())
        session.add(new_class)
        session.commit()
        session.refresh(new_class)
        return new_class
@app.post("/ping")
async def ping(req: Request):
    data = await req.json()

    print("Ping received:", data)
    return {"message": "pong"}

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from models.class_models.class_model import Class_Model
# DATABASE_URL = "mysql://root:rootpwd@localhost/edmetrix_db"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()

# # class DreamSign(Base):
# #     __tablename__ = "dream_signs"
# #     id = Column(Integer, primary_key=True, index=True)
# #     name = Column(String(255), unique=True, index=True)

# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # You can restrict this to your React Native app's IP or localhost if needed
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# @app.get("/signs/")
# def get_signs():
#     session = SessionLocal()
#     # signs = session.query(DreamSign).all()
#     print('hello')
#     return {"id": "1", "name": 'hi', "color": "red"}
#     # return [{"id": s.id, "name": s.name, "color": "red"} for s in signs]


# @app.post("/classes/")
# def create_class(data: Class_Model):
#     print('creating class.....')
#     session = SessionLocal()
#     new_class = Class_Model(**data)
#     session.add(new_class)
#     session.commit()
#     session.refresh(new_class)
#     return new_class
#     # return [{"id": s.id, "name": s.name, "color": "red"} for s in signs]