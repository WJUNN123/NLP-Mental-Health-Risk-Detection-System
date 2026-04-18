# classifier.py - Load HuggingFace model and run inference

import streamlit as st
from transformers import pipeline

from config import HF_MODEL


@st.cache_resource
def load_model():
    """Load the HuggingFace model once and cache it."""
    return pipeline("text-classification", model=HF_MODEL, return_all_scores=True)


def classify(text: str) -> dict:
    """
    Run inference on the input text.
    Returns a dict with the top label and its confidence score.
    """
    model = load_model()
    results = model(text, truncation=True, max_length=512)[0]

    # Find the label with the highest score
    top = max(results, key=lambda x: x["score"])

    return {
        "label": top["label"],   # e.g. "offensive" or "not-offensive"
        "confidence": top["score"]
    }
