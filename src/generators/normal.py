from cbc_reference import CBC_REFERENCE
from generators.utils import random_float, random_int
from models.report import Report


def generate_normal(patient):

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

    return Report(

    patient=patient,

    condition="Normal",

    severity="Normal",

    abnormal_parameters=[],

    cbc=cbc

)