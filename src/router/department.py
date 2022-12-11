from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from config import settings
from src.client.storage import StorageClient
from src.model.model import DepartmentIn
from src.model.sqlmodel import Department, get_session
from src.model.storage_stategies.local_strategy import LocalStrategy

router = APIRouter()


@router.post("/departments/", tags=["department"])
async def set_department(
    *, session: Session = Depends(get_session), departments: DepartmentIn
):

    for d in departments.departments:
        db_department = Department.from_orm(d)
        session.add(db_department)
    session.commit()
    session.refresh(db_department)
    return departments


@router.get("/departments/snapshot", tags=["department"])
async def create_snapshot(*, session: Session = Depends(get_session)):
    departments = session.exec(select(Department)).all()

    storage_client = StorageClient(
        strategy=LocalStrategy(
            avro_data_path=settings["General"]["snapshot"]["avro_data_file"],
            avro_schema_path=settings["General"]["snapshot"]["avro_schema_path"],
            avro_schema_file=settings["Deparment"]["snapshot"]["avro_schema_file"],
            file_name=settings["Deparment"]["snapshot"]["avro_file_name"],
        )
    )

    status = storage_client.create_snapshot(data=departments)

    return status
