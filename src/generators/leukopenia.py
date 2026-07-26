from cbc_reference import CBC_REFERENCE
from generators.utils import random_float, random_int
from models.report import Report


def generate_leukopenia(patient):

    gender = patient["gender"].lower()

    cbc = {

        "Hemoglobin": random_float(
            *CBC_REFERENCE["hemoglobin"][gender]["normal"]
        ),

        "WBC": random_int(
            *CBC_REFERENCE["wbc"]["low"]
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

        "Neutrophils": random_int(40, 60),

        "Lymphocytes": random_int(20, 35),

        "Monocytes": random_int(2, 8),

        "Eosinophils": random_int(1, 4),

        "Basophils": random_int(0, 1)

    }

    return Report(

        patient=patient,

        condition="Leukopenia",

        severity="Moderate",

        abnormal_parameters=[
            "WBC"
        ],

        cbc=cbc

    )