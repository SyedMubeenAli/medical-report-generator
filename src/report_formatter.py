from cbc_reference import CBC_REFERENCE

CBC_UNITS = {

    "Hemoglobin": "g/dL",

    "WBC": "/cumm",

    "RBC": "million/cumm",

    "Platelets": "/cumm",

    "MCV": "fL",

    "MCH": "pg",

    "MCHC": "g/dL",

    "Hematocrit": "%",

    "RDW": "%",

    "Neutrophils": "%",

    "Lymphocytes": "%",

    "Monocytes": "%",

    "Eosinophils": "%",

    "Basophils": "%"

}


def get_reference(parameter, gender):

    gender = gender.lower()

    if parameter == "Hemoglobin":
        return CBC_REFERENCE["hemoglobin"][gender]["normal"]

    if parameter == "RBC":
        return CBC_REFERENCE["rbc"][gender]["normal"]

    if parameter == "Hematocrit":
        return CBC_REFERENCE["hematocrit"][gender]["normal"]

    if parameter == "WBC":
        return CBC_REFERENCE["wbc"]["normal"]

    if parameter == "Platelets":
        return CBC_REFERENCE["platelets"]["normal"]

    if parameter == "MCV":
        return CBC_REFERENCE["mcv"]["normal"]

    if parameter == "MCH":
        return CBC_REFERENCE["mch"]["normal"]

    if parameter == "MCHC":
        return CBC_REFERENCE["mchc"]["normal"]

    if parameter == "RDW":
        return CBC_REFERENCE["rdw"]["normal"]

    if parameter == "Neutrophils":
        return (40, 80)

    if parameter == "Lymphocytes":
        return (20, 40)

    if parameter == "Monocytes":
        return (2, 10)

    if parameter == "Eosinophils":
        return (1, 6)

    if parameter == "Basophils":
        return (0, 1)


def get_status(value, reference):

    low, high = reference

    if value < low:
        return "Low"

    if value > high:
        return "High"

    return "Normal"


def format_report(report):

    gender = report.patient["gender"]

    rows = []

    for parameter, value in report.cbc.items():

        reference = get_reference(
            parameter,
            gender
        )

        rows.append({

            "parameter": parameter,
            "value": value,
            "reference": reference,
            "unit": CBC_UNITS[parameter],
            "status": get_status(
                value,
                reference
            )

        })

    return rows