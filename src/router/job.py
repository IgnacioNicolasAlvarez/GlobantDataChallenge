from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.model.sqlmodel import Job, get_session

router = APIRouter()


@router.post("/jobs/", tags=["job"])
async def set_job(*, session: Session = Depends(get_session), job: List[Job] | Job):

    if isinstance(job, list):
        for j in job:
            session.add(j)
    else:
        session.add(job)
    session.commit()
    session.refresh(job)
    return job
