import os

import qrcode


def generate_qr(report):

    os.makedirs("assets/qr", exist_ok=True)

    qr = qrcode.make(
        f"""
Report ID : {report.patient['report_id']}
Patient : {report.patient['name']}
Condition : {report.condition}
Severity : {report.severity}
"""
    )

    path = f"assets/qr/{report.patient['report_id']}.png"

    qr.save(path)

    return path