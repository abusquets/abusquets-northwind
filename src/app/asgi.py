from contextlib import asynccontextmanager
import logging
from typing import AsyncIterator

from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from .app_container import AppContainer
from app.setup_logging import setup_logging
from auth.adapters.api.http.router import router as auth_router
from config import settings
from northwind.adapters.api.http.router import router as northwind_router
from shared.exceptions import APPExceptionError


setup_logging()

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator:
    await AppContainer().cache_repository.init()
    # Start redis connection pool
    yield
    # Stop redis connection pool
    await AppContainer().cache_repository.close()


app = FastAPI(debug=settings.DEBUG, openapi_url=None, lifespan=lifespan)


# @app.middleware('http')
# async def add_process_time_header(request: Request, call_next: Callable[[Request], Response]) -> Response:
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers['X-Process-Time'] = str(process_time)
#     return response


@app.get('/')
async def root() -> dict:
    return {'message': 'Hello World'}


api_app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
    default_response_class=ORJSONResponse,
)

api_app.include_router(auth_router)
api_app.include_router(northwind_router)

app.mount('/api/v1', api_app)


@api_app.exception_handler(APPExceptionError)
async def custom_exception_handler(_: Request, exc: APPExceptionError) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=exc.status_code,
        content={'error': {'code': exc.code, 'message': exc.message}},
    )
