# risk_mapper.py - Map classifier output to risk level

from config import MEDIUM_THRESHOLD


def map_risk(label: str, confidence: float) -> str:
    """
    Map model label + confidence to a risk tier.

    mental/mental-roberta-base labels:
    - 'normal'    -> LOW
    - 'depression', 'anxiety', 'suicidal', 'stress', 'bipolar', 'personality disorder'
      + confidence < 0.70  -> MEDIUM
      + confidence >= 0.70 -> HIGH
    """
    label_lower = label.lower()

    if label_lower == "normal":
        return "LOW"
    elif confidence >= MEDIUM_THRESHOLD:
        return "HIGH"
    else:
        return "MEDIUM"
