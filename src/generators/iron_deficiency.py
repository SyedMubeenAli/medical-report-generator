from cbc_reference import CBC_REFERENCE
from generators.utils import random_float, random_int
from models.report import Report


def generate_iron_deficiency(patient):

    gender = patient["gender"].lower()

    cbc = {

        "Hemoglobin": random_float(
            *CBC_REFERENCE["hemoglobin"][gender]["low"]
        ),

        "WBC": random_int(
            *CBC_REFERENCE["wbc"]["normal"]
        ),

        "RBC": random_float(
            *CBC_REFERENCE["rbc"][gender]["low"]
        ),

        "Platelets": random_int(
            180000,
            450000
        ),

        "MCV": random_float(
            *CBC_REFERENCE["mcv"]["low"]
        ),

        "MCH": random_float(
            *CBC_REFERENCE["mch"]["low"]
        ),

        "MCHC": random_float(
            *CBC_REFERENCE["mchc"]["low"]
        ),

        "Hematocrit": random_float(
            24,
            37
        ),

        "RDW": random_float(
            15,
            21
        ),

        "Neutrophils": random_int(45, 65),

        "Lymphocytes": random_int(25, 40),

        "Monocytes": random_int(2, 8),

        "Eosinophils": random_int(1, 4),

        "Basophils": random_int(0, 1)

    }

    return Report(

    patient=patient,

    condition="Iron Deficiency",

    severity="Moderate",

    abnormal_parameters=[

        "Hemoglobin",

        "RBC",

        "MCV",

        "MCH",

        "MCHC",

        "RDW"

    ],

    cbc=cbc

)