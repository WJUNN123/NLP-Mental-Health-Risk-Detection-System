# classifier.py - Call HuggingFace Inference API

import requests
import streamlit as st

from config import HF_MODEL


def classify(text: str) -> dict:
    """
    Call HuggingFace Inference API to classify the input text.
    Returns a dict with the top label and its confidence score.
    """
    api_url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
    headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
    payload = {"inputs": text}

    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()

    results = response.json()

    # API returns a list of lists: [[{label, score}, ...]]
    if isinstance(results[0], list):
        results = results[0]

    top = max(results, key=lambda x: x["score"])

    return {
        "label": top["label"],
        "confidence": top["score"]
    }
