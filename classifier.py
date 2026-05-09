# classifier.py - Load HuggingFace model directly via transformers
 
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
 
from config import HF_MODEL
 
# Temperature scaling for confidence calibration
# Higher value = softer probabilities (less overconfident)
# Update this value with optimal_temperature from your notebook
TEMPERATURE = 2.0
 
 
@st.cache_resource
def load_model():
    """Load tokenizer and model once and cache it."""
    tokenizer = AutoTokenizer.from_pretrained(HF_MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(HF_MODEL)
    model.eval()
    return tokenizer, model
 
 
def classify(text: str) -> dict:
    """
    Run inference on the input text with temperature scaling.
    Returns a dict with the raw label and calibrated confidence score.
    """
    tokenizer, model = load_model()
 
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
 
    with torch.no_grad():
        outputs = model(**inputs)
 
    # Apply temperature scaling before softmax
    scaled_logits = outputs.logits / TEMPERATURE
    probs = F.softmax(scaled_logits, dim=-1)[0]
 
    top_idx = probs.argmax().item()
    id2label = model.config.id2label
 
    return {
        "label": id2label[top_idx],       # e.g. LABEL_0, LABEL_1, LABEL_2, LABEL_3
        "confidence": probs[top_idx].item()
    }
