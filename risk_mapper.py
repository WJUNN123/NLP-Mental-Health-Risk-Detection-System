# risk_mapper.py - Map classifier output to risk level

# ourafla/mental-health-bert-finetuned label mapping:
# LABEL_0 = Anxiety
# LABEL_1 = Depression
# LABEL_2 = Normal
# LABEL_3 = Suicidal

LABEL_MAP = {
    "LABEL_0": "Anxiety",
    "LABEL_1": "Depression",
    "LABEL_2": "Normal",
    "LABEL_3": "Suicidal"
}

RISK_MAP = {
    "Normal":     "LOW",
    "Anxiety":    "MEDIUM",
    "Depression": "HIGH",
    "Suicidal":   "HIGH"
}


def map_risk(label: str, confidence: float) -> tuple:
    """
    Translate raw LABEL_X to a human name and risk tier.
    Returns (condition_name, risk_level).
    """
    condition = LABEL_MAP.get(label, label)
    risk_level = RISK_MAP.get(condition, "HIGH")
    return condition, risk_level
