from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from src.api.models.message_models import (
    HealthResponse,
    HomeResponse,
)
from src.api.router import api_router
from src.core.handlers import (
    http_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)
from src.core.middleware import RequestLoggingMiddleware
from src.core.security import SecurityHeadersMiddleware
from src.core.settings import settings



app = FastAPI(
    title=settings.PROJECT_NAME,
    description="""
A production-ready REST API for generating, managing, and analyzing Complete Blood Count (CBC) medical reports.

## Features

- Generate realistic CBC reports
- AI-powered medical condition prediction
- PDF, JSON, and CSV export
- QR code generation
- Digital report verification
- Report analytics and statistics
- Search, filter, sorting, and pagination

Developed using FastAPI and Machine Learning.
""",
    version=settings.API_VERSION,
    contact={
        "name": "Syed Mubeen Ali",
        "url": "https://github.com/SyedMubeenAli",
        "email": "mubeenali.dev@gmail.com"
    },
    license_info={
        "name": "MIT License"
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    unhandled_exception_handler,
)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RequestLoggingMiddleware)

app.add_middleware(SecurityHeadersMiddleware)

@app.get(
    "/",
    response_model=HomeResponse,
    tags=["Home"],
    summary="API Status",
    description="Returns the current status of the API."
)
def home():
    return {
        "success": True,
        "message": "AI-Powered Medical Report Generator API is running",
        "version": settings.API_VERSION,
        "api_version": "v1",
        "documentation": "/docs",
        "redoc": "/redoc",
        "base_url": "/api/v1",
    }


@app.get(
    "/health",
    response_model=HealthResponse,
    tags=["Health"],
    summary="Health Check",
    description="Returns the health status of the API."
)
def health():
    return {
        "status": "healthy",
        "service": "AI-Powered Medical Report Generator API",
        "api_version": "v1",
        "version": settings.API_VERSION,
    }