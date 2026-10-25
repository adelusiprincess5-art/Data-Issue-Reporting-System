from fastapi import FastAPI

from database import engine, Base
from models import DataIssue
from routes import router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Data Issue Reporting System"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Data Issue Reporting System is running"
    }