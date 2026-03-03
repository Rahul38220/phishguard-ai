# PhishGuard AI: Multilingual Phishing Email Detection
**Lead Researcher & Developer** | Published in IRJET (Oct 2025)

## 📌 Overview
PhishGuard AI is a specialized framework for detecting phishing attempts in emails across English, Hindi, and Gujarati. By leveraging transformer-based models, it identifies malicious intent in communication that standard filters often miss, especially in code-switched (mixed language) text.

## 🚀 Key Features
- **Email Analysis:** Scans email headers and body text for phishing indicators.
- **Multilingual NLP:** Powered by **XLM-RoBERTa**, specifically fine-tuned to recognize phishing patterns in regional Indian languages.
- **Explainable AI (XAI):** Instead of a simple "Spam" label, the system explains *why* an email is suspicious in the user's native language.

## 📊 Dataset
The model was trained on a consolidated corpus of ~25,000 emails:
- **Source A:** ~5,000 high-density phishing/safe samples.
- **Source B:** ~20,000 diverse email datasets (Spam vs. Ham).
- **Custom Layer:** Integrated multilingual samples to validate Gujarati and Hindi detection.

## 🛠 Tech Stack
- **AI/ML:** Python, PyTorch, HuggingFace (XLM-RoBERTa)
- **Extension:** JavaScript (UI for submitting/viewing email analysis)
- **Backend:** Python (FastAPI/Flask) to process the ML inference.

## 📁 Repository Structure
- `backend/`: Core AI model, inference API, and text preprocessing.
- `extension/`: Frontend interface for user interaction.
- `shared/`: Logic shared between the interface and the server.
- `storage/`: Database/Log handling for analyzed samples.
- `run.sh`: Shell script for one-click environment setup.
