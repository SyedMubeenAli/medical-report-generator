import json
import os

from src.core.settings import settings
from src.logger import logger

JSON_FOLDER = settings.JSON_FOLDER


def get_json_path(report_id: str):

    return os.path.join(
        JSON_FOLDER,
        f"{report_id}.json"
    )


def load_report(report_id: str):
    file_path = get_json_path(report_id)

    logger.info("Loading report: %s", report_id)

    if not os.path.exists(file_path):
        logger.warning("Report not found: %s", report_id)
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            report = json.load(file)

        logger.info("Report loaded successfully: %s", report_id)
        return report

    except Exception:
        logger.exception("Failed to load report: %s", report_id)
        raise


def save_report(report_id: str, report: dict):
    os.makedirs(JSON_FOLDER, exist_ok=True)

    file_path = get_json_path(report_id)

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False,
            )

        logger.info("Report saved successfully: %s", report_id)

    except Exception:
        logger.exception("Failed to save report: %s", report_id)
        raise


def delete_report_file(report_id: str):
    file_path = get_json_path(report_id)

    if not os.path.exists(file_path):
        logger.warning("Delete failed. Report not found: %s", report_id)
        return False

    try:
        os.remove(file_path)

        logger.info("Report deleted successfully: %s", report_id)
        return True

    except Exception:
        logger.exception("Failed to delete report: %s", report_id)
        raise


def load_all_reports():
    if not os.path.exists(JSON_FOLDER):
        logger.warning("JSON folder does not exist.")
        return []

    reports = []

    for filename in sorted(os.listdir(JSON_FOLDER)):
        if filename.endswith(".json"):
            report_id = filename.replace(".json", "")
            report = load_report(report_id)

            if report:
                reports.append(report)

    logger.info("Loaded %d reports.", len(reports))

    return reports