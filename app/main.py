from contextlib import asynccontextmanager

from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
from app.core.exceptions import InvalidToken, add_exception_handlers
from app.services.notification import NotificationService
from scalar_fastapi import get_scalar_api_reference

from app.api.router import master_router
from app.database.session import create_db_tables


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_db_tables()
    yield


app = FastAPI()
app.include_router(master_router)

add_exception_handlers(app)


@app.get("/mail")
async def send_test_mail(tasks: BackgroundTasks):

    tasks.add_task(
        NotificationService(tasks).send_email,
        recipients=["pyzegv@mailto.plus"],
        subject="Test mail coming through once",
        body="Hello this is vladmir. I eat fluffy dolls and terdy bears for funn. hwahwha😂😂😒",
    )

    return {"detail": "Sending mail..."}


### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
