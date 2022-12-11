from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from config import settings
from src.client.storage import StorageClient
from src.model.model import JobsIn
from src.model.sqlmodel import Job, get_session
from src.model.storage_stategies.local_strategy import LocalStrategy

router = APIRouter()


@router.post("/jobs/", tags=["job"])
async def set_job(*, session: Session = Depends(get_session), jobs: JobsIn):

    for j in jobs.jobs:
        db_job = Job.from_orm(j)
        session.add(db_job)
    session.commit()
    session.refresh(db_job)
    return jobs


@router.get("/jobs/snapshot", tags=["job"])
async def create_snapshot(*, session: Session = Depends(get_session)):
    jobs = session.exec(select(Job)).all()

    storage_client = StorageClient(
        strategy=LocalStrategy(
            avro_data_path=settings["General"]["snapshot"]["avro_data_file"],
            avro_schema_path=settings["General"]["snapshot"]["avro_schema_path"],
            avro_schema_file=settings["Job"]["snapshot"]["avro_schema_file"],
            file_name=settings["Job"]["snapshot"]["avro_file_name"],
        )
    )

    status = storage_client.create_snapshot(data=jobs)

    return status
