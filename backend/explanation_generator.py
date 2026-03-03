
from model_loader import load_explanation_model
import torch

tokenizer, model = load_explanation_model()

def explain_phishing(text, language):
    prompt = f"Explain in {language} why the following email might be a phishing scam: {text}"
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    output_ids = model.generate(**inputs, max_length=100)
    explanation = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return explanation
