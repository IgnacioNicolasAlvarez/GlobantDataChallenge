from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.model.model import JobsIn

from src.model.sqlmodel import Job, get_session

router = APIRouter()


@router.post("/jobs/", tags=["job"])
async def set_job(*, session: Session = Depends(get_session), jobs: JobsIn):

    for j in jobs.jobs:
        db_job = Job.from_orm(j)
        session.add(db_job)
    session.commit()
    session.refresh(db_job)
    return jobs
