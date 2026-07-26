def analyze_cbc(data: dict):

    findings = []

    severity = "Normal"

    hemoglobin = data["Hemoglobin"]
    wbc = data["WBC"]
    platelets = data["Platelets"]

    if hemoglobin < 9:

        findings.append(
            "Hemoglobin is significantly below the normal range."
        )

        severity = "High"

    elif hemoglobin < 12:

        findings.append(
            "Hemoglobin is slightly below the normal range."
        )

        severity = "Moderate"

    if wbc > 11000:

        findings.append(
            "White blood cell count is elevated."
        )

        severity = "High"

    elif wbc < 4000:

        findings.append(
            "White blood cell count is below the normal range."
        )

        severity = "High"

    if platelets < 150000:

        findings.append(
            "Platelet count is below the normal range."
        )

        severity = "High"

    if not findings:

        findings.append(
            "All major CBC parameters are within the normal range."
        )

    return {

        "severity": severity,

        "findings": findings

    }