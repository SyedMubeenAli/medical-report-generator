from fastapi import FastAPI

from src.api.routes.report_routes import router as report_router

app = FastAPI(
    title="AI Diagnostics API",
    version="1.0.0"
)


app.include_router(report_router)


@app.get("/")

def home():

    return {
        "message": "AI Diagnostics API Running"
    }