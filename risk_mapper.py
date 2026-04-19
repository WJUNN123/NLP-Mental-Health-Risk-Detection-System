# risk_mapper.py - Map classifier output to risk level

def map_risk(label: str, confidence: float) -> str:
    """
    Map ourafla/mental-health-bert-finetuned labels to risk tier.

    Labels: Normal, Anxiety, Depression, Suicidal

    Mapping:
    - Normal     -> LOW
    - Anxiety    -> MEDIUM
    - Depression, Suicidal -> HIGH
    """
    label_lower = label.lower()

    if label_lower == "normal":
        return "LOW"
    elif label_lower == "anxiety":
        return "MEDIUM"
    else:
        return "HIGH"
