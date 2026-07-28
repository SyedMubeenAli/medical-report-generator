from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    PROJECT_NAME: str = "AI-Powered Medical Report Generator API"
    API_VERSION: str = "1.0.0"

    JSON_FOLDER: str = "output/json"
    LOG_FOLDER: str = "output/logs"

    MODEL_PATH: str = "src/models/cbc_model.pkl"
    HOST: str = "0.0.0.0"
    PORT: int = 8000


settings = Settings()

JSON_PATH = Path(settings.JSON_FOLDER)
LOG_PATH = Path(settings.LOG_FOLDER)

JSON_PATH.mkdir(parents=True, exist_ok=True)
LOG_PATH.mkdir(parents=True, exist_ok=True)