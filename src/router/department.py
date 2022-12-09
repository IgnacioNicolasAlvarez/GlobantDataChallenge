from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.model.sqlmodel import Department, get_session

router = APIRouter()


@router.post("/departments/", tags=["department"])
async def set_department(
    *,
    session: Session = Depends(get_session),
    department: List[Department] | Department
):

    if isinstance(department, list):
        for j in department:
            session.add(j)
    else:
        session.add(department)
    session.commit()
    session.refresh(department)
    return department
