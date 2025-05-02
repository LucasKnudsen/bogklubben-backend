from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from botocore.errorfactory import ClientError
import logging

logger = logging.getLogger(__name__)


async def global_exception_handler(request: Request, exc: Exception):
    msg = str(exc) or "Internal server error"

    logger.error(f"General Error: {exc} - Path: {request.url}")

    return JSONResponse(status_code=500, content={"message": msg})


async def global_http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP Error: {exc.detail} - Path: {request.url}")
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})


async def boto_client_error_handler(request: Request, exc: ClientError):
    msg = exc.response["Error"]["Message"] or "Boto client error"
    status_code = exc.response["ResponseMetadata"]["HTTPStatusCode"] or 500
    code = exc.response["Error"]["Code"] or "Unknown"

    logger.error(
        f"Boto Client Error: Operation: {exc.operation_name}.\nMessage: {str(exc)} - Path: {request.url}"
    )

    return JSONResponse(
        status_code=status_code,
        content={"message": msg, "error_code": code, "operation": exc.operation_name},
    )
