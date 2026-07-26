from src.ai.model_loader import model


FEATURE_NAMES = [
    "Age",
    "Gender",
    "Hemoglobin",
    "WBC",
    "RBC",
    "Platelets",
    "Hematocrit",
    "MCV",
    "MCH",
    "MCHC"
]


def get_feature_importance(top_n=3):

    importances = model.feature_importances_

    ranked = sorted(
        zip(FEATURE_NAMES, importances),
        key=lambda x: x[1],
        reverse=True
    )

    results = []

    for feature, score in ranked[:top_n]:

        results.append(
            {
                "feature": feature,
                "importance": round(score * 100, 2)
            }
        )

    return results