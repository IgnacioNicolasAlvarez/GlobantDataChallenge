from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.model.model import Hired_EmployeeIn
from src.model.sqlmodel import Hired_Employee, get_session

router = APIRouter()


@router.post("/hired_employees/", tags=["hired_employee"])
async def set_department(
    *, session: Session = Depends(get_session), hired_employees: Hired_EmployeeIn
):

    for e in hired_employees.employees:
        db_employee = Hired_Employee.from_orm(e)
        session.add(db_employee)
    session.commit()
    session.refresh(db_employee)
    return hired_employees
