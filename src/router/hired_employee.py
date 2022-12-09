from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.model.sqlmodel import Hired_Employee, get_session

router = APIRouter()


@router.post("/hired_employees/", tags=["hired_employee"])
async def set_hired_employee(
    *,
    session: Session = Depends(get_session),
    hired_employee: List[Hired_Employee] | Hired_Employee
):

    if isinstance(hired_employee, list):
        for j in hired_employee:
            session.add(j)
    else:
        session.add(hired_employee)
    session.commit()
    session.refresh(hired_employee)
    return hired_employee
