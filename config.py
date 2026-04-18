# config.py - All constants and configuration

# HuggingFace Model
HF_MODEL = "cardiffnlp/twitter-roberta-base-offensive"

# Gemini Model
GEMINI_MODEL = "gemini-1.5-flash-latest"

# Risk Thresholds (based on offensive confidence score)
# If label is "not-offensive" -> LOW RISK
# If label is "offensive" and confidence < 0.70 -> MEDIUM RISK
# If label is "offensive" and confidence >= 0.70 -> HIGH RISK
MEDIUM_THRESHOLD = 0.70

# Risk Level Display Config
RISK_CONFIG = {
    "LOW": {
        "label": "🟢 LOW RISK",
        "color": "#2ecc71",
        "description": "No significant mental health concern detected."
    },
    "MEDIUM": {
        "label": "🟡 MEDIUM RISK",
        "color": "#f39c12",
        "description": "Some concerning signals detected. Monitor closely."
    },
    "HIGH": {
        "label": "🔴 HIGH RISK",
        "color": "#e74c3c",
        "description": "High risk signals detected. Immediate attention recommended."
    }
}

# Gemini Prompt Template
GEMINI_PROMPT_TEMPLATE = """
You are a compassionate mental health support assistant.

A user submitted the following text:
\"{text}\"

The system assessed the mental health risk level as: {risk_level}
Confidence: {confidence:.1f}%

Based on this, provide a short, empathetic, and helpful recommendation (2-3 sentences max).
Do NOT diagnose. Be warm and supportive. Suggest professional help if risk is HIGH.
"""
