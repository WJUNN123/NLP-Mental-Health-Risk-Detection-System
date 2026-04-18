# risk_mapper.py - Map classifier output to risk level

from config import MEDIUM_THRESHOLD


def map_risk(label: str, confidence: float) -> str:
    """
    Map model label + confidence to a risk tier.

    Rules:
    - not-offensive              -> LOW
    - offensive + conf < 0.70   -> MEDIUM
    - offensive + conf >= 0.70  -> HIGH
    """
    if "not" in label.lower():
        return "LOW"
    elif confidence >= MEDIUM_THRESHOLD:
        return "HIGH"
    else:
        return "MEDIUM"
