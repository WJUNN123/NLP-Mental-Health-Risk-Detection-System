# classifier.py - Load HuggingFace model and run inference

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

from config import HF_MODEL


@st.cache_resource
def load_model():
    """Load tokenizer and model once and cache it."""
    tokenizer = AutoTokenizer.from_pretrained(HF_MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(HF_MODEL)
    model.eval()
    return tokenizer, model


def classify(text: str) -> dict:
    """
    Run inference on the input text.
    Returns a dict with the top label and its confidence score.
    """
    tokenizer, model = load_model()

    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

    # Run inference (no gradient needed)
    with torch.no_grad():
        outputs = model(**inputs)

    # Convert logits to probabilities
    probs = F.softmax(outputs.logits, dim=-1)[0]

    # Get label names from model config
    id2label = model.config.id2label

    # Find the label with highest probability
    top_idx = probs.argmax().item()

    return {
        "label": id2label[top_idx],       # e.g. "offensive" or "not-offensive"
        "confidence": probs[top_idx].item()
    }
