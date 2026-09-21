import re
from urllib.parse import urlparse

SUSPICIOUS_TLDS = {".xyz", ".top", ".work", ".click", ".loan", ".gq", ".cf"}
HIGH_TARGET_BRANDS = ["paypal", "google", "apple", "microsoft", "netflix", "bank"]

def analyze_url_heuristics(url: str) -> dict:
    """
    Lightweight v2 pre-filter engine to detect structural URL anomalies 
    before passing text payload to XLM-RoBERTa.
    """
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    
    score = 0.0
    reasons = []

    # Check for IP-based URLs
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", domain):
        score += 0.4
        reasons.append("Raw IP address used as hostname.")

    # Check TLD risk
    if any(domain.endswith(tld) for tld in SUSPICIOUS_TLDS):
        score += 0.3
        reasons.append("Suspicious or high-risk TLD detected.")

    # Check Brand Impersonation / Typosquatting in subdomain
    for brand in HIGH_TARGET_BRANDS:
        if brand in domain and not domain.endswith(f"{brand}.com"):
            score += 0.5
            reasons.append(f"Potential impersonation of brand: {brand}")

    return {
        "heuristic_score": min(score, 1.0),
        "flags": reasons,
        "is_suspicious": score >= 0.4
    }
