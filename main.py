import logging
import random
import string
import time

from fastapi import FastAPI, Request

from src.model.sqlmodel import create_db_and_tables
from src.router import department, hired_employee, job, queries

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    logger.info(
        f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code} request path={request.url.path}"
    )

    return response


app.include_router(department.router)
app.include_router(hired_employee.router)
app.include_router(job.router)
app.include_router(queries.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
