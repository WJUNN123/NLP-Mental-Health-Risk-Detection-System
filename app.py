# app.py - Main Streamlit App

import streamlit as st

from preprocessor import preprocess
from classifier import classify
from risk_mapper import map_risk
from recommender import get_recommendation
from config import RISK_CONFIG

st.set_page_config(
    page_title="Mental Health Risk Analyzer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Mental Health Risk Analysis")
st.write("Enter a text below to analyze its mental health risk level.")

user_input = st.text_area(
    label="Your Text",
    placeholder="Type or paste your text here...",
    height=150
)

if st.button("Analyze", type="primary"):

    if not user_input.strip():
        st.warning("Please enter some text before analyzing.")

    else:
        with st.spinner("Analyzing..."):
            try:
                # Step 1: Preprocess
                clean_text = preprocess(user_input)

                # Step 2: Classify
                result = classify(clean_text)
                label = result["label"]
                confidence = result["confidence"]

                # Step 3: Map to condition name + risk tier
                condition, risk_level = map_risk(label, confidence)
                risk_info = RISK_CONFIG[risk_level]

                # Step 4: Gemini recommendation
                recommendation = get_recommendation(clean_text, risk_level, confidence)

                # ── Display Results ───────────────────────────────────
                st.divider()

                st.markdown(
                    f"### Prediction: <span style='color:{risk_info['color']}'>{risk_info['label']}</span>",
                    unsafe_allow_html=True
                )
                st.markdown(f"**Detected Condition:** {condition}")
                st.markdown(f"**Confidence:** {confidence * 100:.1f}%")
                st.progress(confidence)
                st.caption(risk_info["description"])

                st.divider()

                st.markdown("### 📌 Recommendation")
                st.info(recommendation)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
