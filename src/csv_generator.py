import csv
import os


def export_csv(reports):

    os.makedirs(
        "output/csv",
        exist_ok=True
    )

    filename = "output/csv/cbc_reports.csv"

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([

            "Report ID",
            "Patient ID",
            "Name",
            "Age",
            "Gender",
            "Doctor",
            "Condition",
            "Severity",

            "Hemoglobin",
            "WBC",
            "RBC",
            "Platelets",
            "MCV",
            "MCH",
            "MCHC",
            "Hematocrit",
            "RDW",
            "Neutrophils",
            "Lymphocytes",
            "Monocytes",
            "Eosinophils",
            "Basophils"

        ])

        for report in reports:

            patient = report.patient

            cbc = report.cbc

            writer.writerow([

                patient["report_id"],
                patient["patient_id"],
                patient["name"],
                patient["age"],
                patient["gender"],
                patient["doctor"],

                report.condition,
                report.severity,

                cbc["Hemoglobin"],
                cbc["WBC"],
                cbc["RBC"],
                cbc["Platelets"],
                cbc["MCV"],
                cbc["MCH"],
                cbc["MCHC"],
                cbc["Hematocrit"],
                cbc["RDW"],
                cbc["Neutrophils"],
                cbc["Lymphocytes"],
                cbc["Monocytes"],
                cbc["Eosinophils"],
                cbc["Basophils"]

            ])

    print()
    print("CSV file saved in: output/csv/")