import json
import os


JSON_FOLDER = "output/json"


def get_json_path(report_id: str):

    return os.path.join(
        JSON_FOLDER,
        f"{report_id}.json"
    )


def load_report(report_id: str):

    file_path = get_json_path(report_id)

    print("Requested ID:", report_id)
    print("Looking for:", file_path)
    print("Exists:", os.path.exists(file_path))

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_report(report_id: str, report: dict):

    file_path = get_json_path(report_id)

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False
        )


def delete_report_file(report_id: str):

    file_path = get_json_path(report_id)

    if not os.path.exists(file_path):
        return False

    os.remove(file_path)

    return True


def load_all_reports():

    reports = []

    for filename in sorted(os.listdir(JSON_FOLDER)):

        if filename.endswith(".json"):

            report_id = filename.replace(".json", "")

            report = load_report(report_id)

            if report:

                reports.append(report)

    return reports