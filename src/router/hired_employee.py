from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from config import settings
from src.client.storage import StorageClient
from src.model.model import Hired_EmployeeIn
from src.model.sqlmodel import Hired_Employee, get_session
from src.model.storage_stategies.local_strategy import LocalStrategy

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


@router.get("/hired_employees/snapshot", tags=["department"])
async def create_snapshot(*, session: Session = Depends(get_session)):
    hired_employees = session.exec(select(Hired_Employee)).all()

    storage_client = StorageClient(
        strategy=LocalStrategy(
            avro_data_path=settings["General"]["snapshot"]["avro_data_file"],
            avro_schema_file=settings["General"]["snapshot"]["avro_schema_file"],
            file_name=settings["Hired_Employee"]["snapshot"]["avro_file_name"],
        )
    )

    status = storage_client.create_snapshot(data=hired_employees)

    return status
