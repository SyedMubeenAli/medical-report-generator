from cbc_generator import generate_cbc
from patient_generator import generate_patient
from report_formatter import format_report

patient = generate_patient(1)

report = generate_cbc(
    patient,
    "Iron Deficiency"
)

rows = format_report(report)

for row in rows:
    print(row)