
from fastapi import FastAPI
from pydantic import BaseModel
from phishing_classifier import classify_text
from explanation_generator import explain_phishing
from shared.lang_detect import detect_language
from v2.heuristics import analyze_url_heuristics

app = FastAPI()

class EmailRequest(BaseModel):
    text: str

@app.post("/classify")
def classify_email(req: EmailRequest):
    lang = detect_language(req.text)
    label = classify_text(req.text)
    return {"label": label, "language": lang}

@app.post("/explain")
def explain_email(req: EmailRequest):
    lang = detect_language(req.text)
    explanation = explain_phishing(req.text, lang)
    return {"explanation": explanation, "language": lang}

@app.post("/api/v2/analyze-url")
async def analyze_url_v2(url: str):
    """v2 Endpoint: Fast-path heuristic analysis combining rule engine with DL."""
    results = analyze_url_heuristics(url)
    return {"status": "success", "data": results}
