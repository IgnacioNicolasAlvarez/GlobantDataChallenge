from typing import Optional

from sqlmodel import Field, SQLModel
from datetime import datetime


class Job(SQLModel, table=True):
    job_id: Optional[int] = Field(default=None, primary_key=True)
    job: str
    
    
    
class Department(SQLModel, table=True):
    department_id: Optional[int] = Field(default=None, primary_key=True)
    deparment: str
    
    

class HiredEmployee(SQLModel, table=True):
    hired_employee_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    datetime : datetime
    department_id: int = Field(default=None, foreign_key="department.department_id")
    job_id: int = Field(default=None, foreign_key="job.job_id")
    