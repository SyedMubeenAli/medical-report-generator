def generate_explanation(condition: str):

    explanations = {

        "Normal": {

            "severity": "Normal",

            "summary":
            "All major CBC parameters are within the normal reference ranges.",

            "recommendation":
            "Continue maintaining a healthy lifestyle and routine medical checkups."

        },

        "Anemia": {

            "severity": "Moderate",

            "summary":
            "The hemoglobin level is below the normal range, suggesting Anemia.",

            "recommendation":
            "Consult a physician for further evaluation and possible iron studies."

        },

        "Leukocytosis": {

            "severity": "Moderate",

            "summary":
            "The white blood cell count is elevated, suggesting Leukocytosis.",

            "recommendation":
            "Further clinical evaluation is recommended to identify the underlying cause."

        },

        "Leukopenia": {

            "severity": "Moderate",

            "summary":
            "The white blood cell count is below the normal range, suggesting Leukopenia.",

            "recommendation":
            "Consult a healthcare provider for additional laboratory investigations."

        },

        "Thrombocytopenia": {

            "severity": "High",

            "summary":
            "The platelet count is lower than the normal range, suggesting Thrombocytopenia.",

            "recommendation":
            "Medical consultation is advised to assess bleeding risk and determine appropriate treatment."

        }

    }

    return explanations.get(
        condition,
        {
            "severity": "Unknown",
            "summary": "No explanation available.",
            "recommendation": "Consult a healthcare provider."
        }
    )