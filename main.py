
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, create_engine, Session

from _models import *
from _models.base import Base

from routers import *

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
app.include_router(classes_router)
app.include_router(students_router)
app.include_router(seating_charts_router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

