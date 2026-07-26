import json

from pathlib import Path

from report_formatter import format_report

def export_reports_to_json(reports):

    output_dir = Path("output/json")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    for report in reports:

        rows = format_report(report)

        report_json = {

            "patient": report.patient,

            "condition": report.condition,

            "severity": report.severity,

            "abnormal_parameters": report.abnormal_parameters,

            "cbc": rows

        }

        filename = (
            f"{report.patient['report_id']}.json"
        )

        filepath = output_dir / filename

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report_json,
                file,
                indent=4
            )

    print()

    print(
        f"JSON files saved in: {output_dir}"
    )