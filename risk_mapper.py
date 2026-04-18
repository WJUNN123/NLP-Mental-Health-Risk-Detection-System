# risk_mapper.py - Map classifier output to risk level

def map_risk(label: str, confidence: float) -> str:
    """
    Map model label to risk tier.

    paulagarciaserrano/roberta-depression-detection labels:
    - "not depression" -> LOW
    - "moderate"       -> MEDIUM
    - "severe"         -> HIGH
    """
    label_lower = label.lower()

    if "not" in label_lower:
        return "LOW"
    elif "moderate" in label_lower:
        return "MEDIUM"
    else:
        return "HIGH"
