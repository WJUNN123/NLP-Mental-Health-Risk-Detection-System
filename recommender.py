# recommender.py - Generate advice using Gemini
 
from google import genai
import streamlit as st
 
from config import GEMINI_MODEL, GEMINI_PROMPT_TEMPLATE
 
 
def get_recommendation(text: str, risk_level: str, confidence: float) -> str:
    """Call Gemini to generate a recommendation based on risk level."""
 
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
 
    prompt = GEMINI_PROMPT_TEMPLATE.format(
        text=text,
        risk_level=risk_level,
        confidence=confidence * 100
    )
 
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        return response.text.strip()
 
    except Exception as e:
        if "429" in str(e) or "quota" in str(e).lower():
            return "⚠️ Gemini API quota exceeded. Please try again later."
        return f"⚠️ Could not generate recommendation. Please try again."
