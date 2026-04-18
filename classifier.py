# classifier.py - Load HuggingFace model and run inference

import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification, AutoConfig
import torch
import torch.nn.functional as F

from config import HF_MODEL


@st.cache_resource
def load_model():
    """Load tokenizer and model once and cache it."""
    config = AutoConfig.from_pretrained(HF_MODEL, num_labels=6, problem_type="single_label_classification")
    tokenizer = BertTokenizer.from_pretrained(HF_MODEL, use_fast=True)
    model = BertForSequenceClassification.from_pretrained(HF_MODEL, config=config, ignore_mismatched_sizes=True)
    model.eval()
    return tokenizer, model


def classify(text: str) -> dict:
    """
    Run inference on the input text.
    Returns a dict with the top label (severity 0-5) and confidence score.
    """
    tokenizer, model = load_model()

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = F.softmax(outputs.logits, dim=-1)[0]
    top_idx = probs.argmax().item()

    return {
        "label": str(top_idx),           # severity level 0-5
        "confidence": probs[top_idx].item()
    }
