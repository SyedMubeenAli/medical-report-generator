import random

from patient_generator import generate_patient
from cbc_reference import CBC_REFERENCE


def random_float(low, high, digits=1):
    return round(random.uniform(low, high), digits)


def random_int(low, high):
    return random.randint(low, high)


def generate_normal_cbc(patient):

    gender = patient["gender"].lower()

    cbc = {

        "Hemoglobin": random_float(
            *CBC_REFERENCE["hemoglobin"][gender]["normal"]
        ),

        "WBC": random_int(
            *CBC_REFERENCE["wbc"]["normal"]
        ),

        "RBC": random_float(
            *CBC_REFERENCE["rbc"][gender]["normal"]
        ),

        "Platelets": random_int(
            *CBC_REFERENCE["platelets"]["normal"]
        ),

        "MCV": random_float(
            *CBC_REFERENCE["mcv"]["normal"]
        ),

        "MCH": random_float(
            *CBC_REFERENCE["mch"]["normal"]
        ),

        "MCHC": random_float(
            *CBC_REFERENCE["mchc"]["normal"]
        ),

        "Hematocrit": random_float(
            *CBC_REFERENCE["hematocrit"][gender]["normal"]
        ),

        "RDW": random_float(
            *CBC_REFERENCE["rdw"]["normal"]
        ),

        "Neutrophils": random_int(
            *CBC_REFERENCE["neutrophils"]["normal"]
        ),

        "Lymphocytes": random_int(
            *CBC_REFERENCE["lymphocytes"]["normal"]
        ),

        "Monocytes": random_int(
            *CBC_REFERENCE["monocytes"]["normal"]
        ),

        "Eosinophils": random_int(
            *CBC_REFERENCE["eosinophils"]["normal"]
        ),

        "Basophils": random_int(
            *CBC_REFERENCE["basophils"]["normal"]
        )

    }

    return cbc


if __name__ == "__main__":

    patient = generate_patient(1)

    report = generate_normal_cbc(patient)

    print(patient)

    print()

    for key, value in report.items():
        print(f"{key:15}: {value}")