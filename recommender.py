# recommender.py - Generate advice using Gemini

import google.generativeai as genai
import streamlit as st

from config import GEMINI_MODEL, GEMINI_PROMPT_TEMPLATE


def get_recommendation(text: str, risk_level: str, confidence: float) -> str:
    """Call Gemini to generate a recommendation based on risk level."""

    # Load API key from Streamlit secrets
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel(GEMINI_MODEL)

    prompt = GEMINI_PROMPT_TEMPLATE.format(
        text=text,
        risk_level=risk_level,
        confidence=confidence * 100
    )

    response = model.generate_content(prompt)
    return response.text.strip()
