from cbc_reference import CBC_REFERENCE
from generators.utils import random_float, random_int
from models.report import Report


def generate_viral_infection(patient):

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

        "Neutrophils": random_int(35, 45),

        "Lymphocytes": random_int(45, 60),

        "Monocytes": random_int(2, 8),

        "Eosinophils": random_int(1, 4),

        "Basophils": random_int(0, 1)

    }

    return Report(

        patient=patient,

        condition="Viral Infection",

        severity="Moderate",

        abnormal_parameters=[
            "WBC",
            "Lymphocytes"
        ],

        cbc=cbc

    )