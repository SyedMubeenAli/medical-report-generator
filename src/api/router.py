from fastapi import APIRouter

from src.api.routes.report_routes import router as report_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(report_router)