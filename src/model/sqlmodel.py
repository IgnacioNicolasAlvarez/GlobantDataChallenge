from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session
from config import settings

SQLModel.metadata.clear()


class Job(SQLModel, table=True):

    job_id: Optional[int] = Field(default=None, primary_key=True)
    job: str


class Department(SQLModel, table=True):

    department_id: Optional[int] = Field(default=None, primary_key=True)
    deparment: str


class Hired_Employee(SQLModel, table=True):

    hired_employee_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    datetime: datetime
    department_id: int = Field(default=None, foreign_key="department.department_id")
    job_id: int = Field(default=None, foreign_key="job.job_id")


engine = create_engine(settings["DB"]["conn_str"], echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
