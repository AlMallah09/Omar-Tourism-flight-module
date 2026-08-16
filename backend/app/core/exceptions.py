import logging

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


logger = logging.getLogger(__name__)


async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        headers=exc.headers,
        content={
            "error": {
                "status_code": exc.status_code,
                "message": exc.detail
            }
        }
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = []

    for error in exc.errors():
        errors.append({
            "field": ".".join(
                str(location)
                for location in error["loc"]
            ),
            "message": error["msg"],
            "type": error["type"]
        })

    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "status_code": 422,
                "message": "Request validation failed",
                "details": errors
            }
        }
    )


async def unexpected_exception_handler(
    request: Request,
    exc: Exception
):
    logger.exception(
        "Unhandled exception while processing %s %s",
        request.method,
        request.url.path,
        exc_info=exc
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "status_code": 500,
                "message": "Internal server error"
            }
        }
    )