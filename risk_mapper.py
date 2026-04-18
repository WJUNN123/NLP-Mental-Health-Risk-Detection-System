# risk_mapper.py - Map classifier output to risk level

from config import LOW_MAX, MEDIUM_MAX


def map_risk(label: str, confidence: float) -> str:
    """
    Map model label to risk tier.

    KevSun/mentalhealth_LM labels are severity scores 0-5:
    - 0-1 -> LOW
    - 2-3 -> MEDIUM
    - 4-5 -> HIGH
    """
    try:
        severity = int(label)
    except (ValueError, TypeError):
        # Fallback if label is not numeric
        severity = 3

    if severity <= LOW_MAX:
        return "LOW"
    elif severity <= MEDIUM_MAX:
        return "MEDIUM"
    else:
        return "HIGH"
