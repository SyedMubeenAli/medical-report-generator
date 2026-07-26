import json
import os
from collections import Counter
from statistics import mean


def export_dataset_analysis(reports):

    gender_counts = Counter()
    condition_counts = Counter()
    severity_counts = Counter()
    abnormal_counts = Counter()

    ages = []

    for report in reports:

        gender_counts[report.patient["gender"]] += 1
        condition_counts[report.condition] += 1
        severity_counts[report.severity] += 1

        ages.append(report.patient["age"])

        abnormal_counts.update(report.abnormal_parameters)

    summary = {

        "total_reports": len(reports),

        "gender_distribution": dict(gender_counts),

        "condition_distribution": dict(condition_counts),

        "severity_distribution": dict(severity_counts),

        "age_statistics": {

            "minimum": min(ages),

            "maximum": max(ages),

            "average": round(mean(ages), 2)

        },

        "abnormal_parameters": dict(abnormal_counts)

    }

    os.makedirs(
        "output/analytics",
        exist_ok=True
    )

    with open(
        "output/analytics/dataset_summary.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            summary,
            file,
            indent=4
        )

    print("\nAnalytics exported successfully.")