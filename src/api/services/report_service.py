from collections import Counter

from src.api.repositories.report_repository import (
    load_report,
    load_all_reports,
    save_report,
    delete_report_file
)


def get_report(report_id: str):

    return load_report(report_id)


def get_all_reports(
    patient: str = None,
    condition: str = None,
    sort_by: str = None,
    order: str = "asc"
):

    all_reports = load_all_reports()

    reports = []

    for report in all_reports:

        patient_name = report["patient"]["name"]
        report_condition = report["condition"]

        if patient:

            if patient.lower() not in patient_name.lower():
                continue

        if condition:

            if condition.lower() != report_condition.lower():
                continue

        reports.append({

            "report_id": report["patient"]["report_id"],
            "patient_name": patient_name,
            "age": report["patient"]["age"],
            "gender": report["patient"]["gender"],
            "condition": report_condition,
            "severity": report["severity"]

        })

    if sort_by:

        allowed_fields = [
            "age",
            "patient_name",
            "condition",
            "severity"
        ]

        if sort_by in allowed_fields:

            reverse = order.lower() == "desc"

            reports = sorted(
                reports,
                key=lambda x: x[sort_by],
                reverse=reverse
            )

    return reports


def get_statistics():

    reports = get_all_reports()

    total_reports = len(reports)

    gender_counter = Counter()
    condition_counter = Counter()

    total_age = 0

    for report in reports:

        gender_counter[report["gender"]] += 1
        condition_counter[report["condition"]] += 1
        total_age += report["age"]

    average_age = round(total_age / total_reports, 1) if total_reports else 0

    return {

        "total_reports": total_reports,
        "average_age": average_age,
        "male": gender_counter["Male"],
        "female": gender_counter["Female"],
        "conditions": dict(condition_counter)

    }


def delete_report(report_id: str):

    return delete_report_file(report_id)


def update_report(report_id: str, updated_data: dict):

    report = load_report(report_id)

    if report is None:
        return None

    report["patient"]["name"] = updated_data["patient_name"]
    report["patient"]["age"] = updated_data["age"]
    report["patient"]["gender"] = updated_data["gender"]

    report["condition"] = updated_data["condition"]
    report["severity"] = updated_data["severity"]

    save_report(report_id, report)

    return report