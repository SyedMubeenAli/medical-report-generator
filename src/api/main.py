from fastapi import FastAPI

from src.api.routes.report_routes import router as report_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI-Powered Medical Report Generator API",
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
    version="1.0.0",
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

app.include_router(report_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/",
    tags=["Home"],
    summary="API Status",
    description="Returns the current status of the API."
)
def home():
    return {
        "success": True,
        "message": "AI-Powered Medical Report Generator API is running",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get(
    "/health",
    tags=["Health"],
    summary="Health Check",
    description="Returns the health status of the API."
)
def health():

    return {
        "status": "healthy",
        "service": "AI-Powered Medical Report Generator API",
        "version": "1.0.0"
    }