from datetime import datetime

from pydantic import BaseModel, conlist


class Job(BaseModel):

    job_id: int
    job: str


class JobsIn(BaseModel):

    jobs: conlist(Job, min_items=1, max_items=1000)


class Department(BaseModel):

    department_id: int
    deparment: str


class DepartmentIn(BaseModel):

    departments: conlist(Department, min_items=1, max_items=1000)


class Hired_Employee(BaseModel):

    hired_employee_id: int
    name: str
    datetime: datetime
    department_id: int
    job_id: int


class Hired_EmployeeIn(BaseModel):

    employees: conlist(Hired_Employee, min_items=1, max_items=1000)


class Query_output_Department_Job_Count(BaseModel):
    department: str
    job: str
    employee_count: int
    hire_quarter: str
