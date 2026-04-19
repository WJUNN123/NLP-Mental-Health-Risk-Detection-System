# risk_mapper.py - Map classifier output to risk level

def map_risk(label: str, confidence: float) -> str:
    """
    Map mental/mental-roberta-base labels to risk tier.

    Labels: normal, depression, anxiety, bipolar, stress,
            personality disorder, suicidal

    Mapping:
    - normal                          -> LOW
    - stress, anxiety                 -> MEDIUM
    - depression, bipolar,
      personality disorder, suicidal  -> HIGH
    """
    label_lower = label.lower()

    if label_lower == "normal":
        return "LOW"
    elif label_lower in ("stress", "anxiety"):
        return "MEDIUM"
    else:
        return "HIGH"
