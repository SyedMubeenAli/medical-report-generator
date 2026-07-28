import random

from analytics.charts import generate_charts
from analytics.dataset_analysis import analyze_dataset
from analytics.export_analysis import export_dataset_analysis
from cbc_generator import generate_cbc
from csv_generator import export_csv
from export_json import export_reports_to_json
from logger import logger
from patient_generator import generate_patient
from pdf_generator import generate_pdf
from qr_generator import generate_qr
from validators.report_validator import validate_report
from verification.html_generator import generate_verification_page

CONDITION_COUNTS = {
    "Normal": 10,
    "Iron Deficiency": 8,
    "Leukocytosis": 8,
    "Leukopenia": 8,
    "Viral Infection": 8,
    "Thrombocytopenia": 8
}


def build_condition_list():

    conditions = []

    for condition, count in CONDITION_COUNTS.items():
        conditions.extend([condition] * count)

    random.shuffle(conditions)

    return conditions


def generate_dataset():

    reports = []

    conditions = build_condition_list()

    for index, condition in enumerate(conditions, start=1):

        patient = generate_patient(index)

        report = generate_cbc(
            patient,
            condition
        )

        validate_report(report)

        generate_qr(report)

        reports.append(report)

    return reports


if __name__ == "__main__":

    logger.info("Starting dataset generation...")

    reports = generate_dataset()

    print("=" * 50)
    print("Dataset Generated Successfully")
    print(f"Total Reports : {len(reports)}")

    counts = {}

    for report in reports:
        counts[report.condition] = counts.get(report.condition, 0) + 1

    for key, value in counts.items():
        print(f"{key:20}: {value}")

    export_reports_to_json(reports)

    export_csv(reports)

    analyze_dataset(reports)

    export_dataset_analysis(reports)

    generate_charts(reports)

    for report in reports:
        generate_pdf(report)
        generate_verification_page(report)

    

    logger.info("Dataset generation completed successfully.")

    print("=" * 50)
