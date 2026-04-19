# risk_mapper.py - Map classifier output to risk level

def map_risk(label: str, confidence: float) -> str:
    """
    Map Elite13/bert-finetuned-mental-health labels to risk tier.

    Labels: Normal, Anxiety, Stress, Depression, Bipolar,
            Personality Disorder, Suicidal

    Mapping:
    - Normal                              -> LOW
    - Anxiety, Stress                     -> MEDIUM
    - Depression, Bipolar,
      Personality Disorder, Suicidal      -> HIGH
    """
    label_lower = label.lower()

    if label_lower == "normal":
        return "LOW"
    elif label_lower in ("anxiety", "stress"):
        return "MEDIUM"
    else:
        return "HIGH"
