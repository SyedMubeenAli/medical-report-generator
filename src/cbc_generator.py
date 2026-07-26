import random

from patient_generator import generate_patient
from conditions import CBC_CONDITIONS

from generators.dispatcher import GENERATOR_MAP


def generate_condition():
    return random.choice(CBC_CONDITIONS)

def generate_cbc(patient, condition):

    generator = GENERATOR_MAP.get(condition)

    if generator is None:
        raise ValueError(f"Unknown condition: {condition}")

    return generator(patient)

if __name__ == "__main__":
    patient = generate_patient(1)
    report = generate_cbc(
    patient,
    "Thrombocytopenia"
)

    print()
    print(patient)
    print()
    print("Condition :", report.condition)

    print("Severity :", report.severity)
    print()

    for key, value in report.cbc.items():
        print(f"{key:15}: {value}")