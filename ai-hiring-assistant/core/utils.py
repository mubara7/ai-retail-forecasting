import re
from typing import List, Set

STOPWORDS: Set[str] = {
    "a","an","the","and","or","but","if","then","else","for","to","of","in","on","at","by","with",
    "is","are","was","were","be","been","being","as","it","this","that","these","those","from",
    "we","you","they","i","he","she","them","our","your","their","my"
}

def clean_text(text: str) -> str:
    text = text or ""
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"[^a-z0-9+\#\s]", " ", text)  # keep c++, c#, etc
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize(text: str) -> List[str]:
    text = clean_text(text)
    tokens = [t for t in text.split() if t and t not in STOPWORDS and len(t) > 1]
    return tokens

def to_set(tokens: List[str]) -> Set[str]:
    return set(tokens)
