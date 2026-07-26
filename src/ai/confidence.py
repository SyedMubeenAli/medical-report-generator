def get_confidence_level(confidence: float):

    if confidence >= 95:
        return "Very High"

    if confidence >= 85:
        return "High"

    if confidence >= 70:
        return "Moderate"

    return "Low"