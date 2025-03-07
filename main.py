from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://oneira:oneirapwd1!@localhost/oneira_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class DreamSign(Base):
    __tablename__ = "dream_signs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your React Native app's IP or localhost if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/signs/")
def get_signs():
    session = SessionLocal()
    # signs = session.query(DreamSign).all()
    print('hello')
    return {"id": "1", "name": 'hi', "color": "red"}
    # return [{"id": s.id, "name": s.name, "color": "red"} for s in signs]