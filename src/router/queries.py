from fastapi import APIRouter, Depends
from sqlmodel import Session

from config import settings
from src.client.db import SQLTemplateExecutor

from src.model.model import Query_output_Department_Job_Count
from src.model.sqlmodel import get_session


router = APIRouter()


@router.get("/queries/count_by_job_department", tags=["queries"])
async def get_count_by_job_department(*, session: Session = Depends(get_session)):

    sql_executor = SQLTemplateExecutor(
        session=session,
        template_file=settings["SQL"]["count_by_job_deparment"]["template_file"],
        template_path=settings["SQL"]["count_by_job_deparment"]["template_path"],
    )
    result = sql_executor.execute(
        select_year=settings["SQL"]["count_by_job_deparment"]["parameters"][
            "select_year"
        ]
    )

    result = [Query_output_Department_Job_Count(**r) for r in result]
    return result
