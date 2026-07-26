import hashlib


def generate_signature(report):

    raw_data = (

        report.patient["report_id"]

        + report.patient["patient_id"]

        + report.patient["name"]

        + report.condition

        + report.severity

    )

    signature = hashlib.sha256(

        raw_data.encode()

    ).hexdigest()

    return signature