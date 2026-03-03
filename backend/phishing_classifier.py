
from model_loader import load_classification_model
import torch

tokenizer, model = load_classification_model()

def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    scores = torch.nn.functional.softmax(outputs.logits, dim=1)
    label = torch.argmax(scores).item()
    return "phishing" if label == 1 else "safe"
