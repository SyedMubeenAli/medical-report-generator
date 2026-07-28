import logging
from logging.handlers import RotatingFileHandler

from src.core.settings import LOG_PATH

LOG_DIR = LOG_PATH

LOG_DIR.mkdir(parents=True, exist_ok=True)

APP_LOG = LOG_DIR / "app.log"
ERROR_LOG = LOG_DIR / "error.log"

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logger = logging.getLogger("MedicalReportGenerator")
logger.setLevel(logging.INFO)

if not logger.handlers:

    app_handler = RotatingFileHandler(
        APP_LOG,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )

    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    error_handler = RotatingFileHandler(
        ERROR_LOG,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )

    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

logger.propagate = False