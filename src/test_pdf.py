from cbc_generator import generate_cbc
from patient_generator import generate_patient
from pdf_generator import generate_pdf

patient = generate_patient(1)

report = generate_cbc(
    patient,
    "Thrombocytopenia"
)

generate_pdf(report)

print()
print("PDF Generated Successfully")