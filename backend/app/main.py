import logging
import time
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.config import settings
from app.core.logging_config import configure_logging
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    unexpected_exception_handler
)

from app.flights.routes import router as flights_router
from app.users.routes import router as users_router
from app.bookings.routes import router as bookings_router
from app.authentication.routes import router as authentication_router
from app.passengers.routes import router as passengers_router
from app.admin.routes import router as admin_router
from app.analytics.routes import router as analytics_router
from app.reports.routes import router as reports_router


configure_logging()

logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(
        "Application started",
        extra={
            "environment": settings.ENVIRONMENT
        }
    )

    yield

    logger.info(
        "Application stopped",
        extra={
            "environment": settings.ENVIRONMENT
        }
    )

app = FastAPI(
    title="Omar Tourism Flight Module API",
    version="1.0.0",
    allowed_hosts=settings.ALLOWED_HOSTS
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unexpected_exception_handler)

@app.middleware("http")
async def request_logging_middleware(
    request: Request,
    call_next
):
    request_id = str(uuid.uuid4())

    start_time = time.perf_counter()

    try:
        response = await call_next(request)

        duration_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        logger.info(
            "Request completed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration_ms
            }
        )

        response.headers["X-Request-ID"] = request_id

        return response

    except Exception:
        duration_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        logger.exception(
            "Request failed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "duration_ms": duration_ms
            }
        )

        raise

@app.middleware("http")
async def security_headers_middleware(
    request: Request,
    call_next
):
    response = await call_next(request)

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"

    return response

api_v1_router = APIRouter(
    prefix=settings.API_V1_PREFIX
)

api_v1_router.include_router(flights_router)
api_v1_router.include_router(users_router)
api_v1_router.include_router(bookings_router)
api_v1_router.include_router(authentication_router)
api_v1_router.include_router(passengers_router)
api_v1_router.include_router(admin_router)
api_v1_router.include_router(analytics_router)
api_v1_router.include_router(reports_router)

app.include_router(api_v1_router)

@app.get("/")
def root():
    return {"message": "Omar Tourism API is running"}
