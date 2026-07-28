from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.logger import logger


async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(
        "HTTP %s | %s | %s",
        exc.status_code,
        request.url.path,
        exc.detail,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.status_code,
                "message": exc.detail,
            },
        },
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    logger.warning(
        "Validation Error | %s",
        request.url.path,
    )

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "code": 422,
                "message": "Validation failed",
                "details": exc.errors(),
            },
        },
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        "Unhandled Exception | %s",
        request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": 500,
                "message": "Internal server error",
            },
        },
    )