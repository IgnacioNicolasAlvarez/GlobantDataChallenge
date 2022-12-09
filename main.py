from fastapi import FastAPI

from src.model.sqlmodel import create_db_and_tables
from src.router import department, hired_employee, job

app = FastAPI()

app.include_router(department.router)
app.include_router(hired_employee.router)
app.include_router(job.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
