# preprocessor.py - Clean and normalize input text

import re

def preprocess(text: str) -> str:
    """Clean and normalize user input text."""

    # Strip leading/trailing whitespace
    text = text.strip()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text)

    return text
