# config.py - All constants and configuration

# HuggingFace Model
# KevSun/mentalhealth_LM: public BERT model, labels 0-5 (0=minimal, 5=severe)
HF_MODEL = "KevSun/mentalhealth_LM"

# Gemini Model
GEMINI_MODEL = "gemini-2.5-flash"

# Risk Thresholds based on severity score (0-5)
# 0-1 -> LOW, 2-3 -> MEDIUM, 4-5 -> HIGH
LOW_MAX = 1
MEDIUM_MAX = 3

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
