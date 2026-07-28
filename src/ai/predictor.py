import pandas as pd

from src.ai.analyzer import analyze_cbc
from src.ai.confidence import get_confidence_level
from src.ai.explanation import generate_explanation
from src.ai.feature_importance import get_feature_importance
from src.ai.model_loader import gender_encoder, label_encoder, model

FEATURE_ORDER = [
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


def predict_condition(data: dict):

    dataframe = pd.DataFrame([data])

    dataframe["Gender"] = gender_encoder.transform(
        dataframe["Gender"]
    )

    dataframe = dataframe[FEATURE_ORDER]

    prediction = model.predict(dataframe)[0]

    probabilities = model.predict_proba(dataframe)[0]

    confidence = round(
        max(probabilities) * 100,
        2
    )

    confidence_level = get_confidence_level(
        confidence
    )

    predicted_condition = label_encoder.inverse_transform(
        [prediction]
    )[0]

    explanation = generate_explanation(
        predicted_condition
    )

    analysis = analyze_cbc(data)

    important_features = get_feature_importance()

    return {

        "prediction": predicted_condition,

        "confidence": confidence,

        "confidence_level": confidence_level,

        "severity": analysis["severity"],

        "findings": analysis["findings"],

        "summary": explanation["summary"],

        "recommendation": explanation["recommendation"],

        "important_features": important_features

}