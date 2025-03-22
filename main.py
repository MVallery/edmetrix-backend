
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, create_engine, Session
# import model folders
from user.models import *
from auth.models import *
from school.models import *
from classes.models import *
from classes.seating_charts.models import *
from classes.group.models import *

from students.models import *
from metrix.models import *
from _models.base import Base

from classes.routes import router as classes_router
from classes.seating_charts.routes import router as seating_charts_router
# from students.routes import router as students_router
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
app.include_router(seating_charts_router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

