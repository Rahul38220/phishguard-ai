# PhishGuard AI: Phishing Email Detection Framework
**Lead Researcher & Developer** | Published in IRJET (Oct 2025)

## 📌 Overview
PhishGuard AI is an AI-driven framework designed to identify and classify phishing attempts within email communications. By utilizing transformer-based NLP models, the system distinguishes between legitimate "Ham" and malicious "Phishing" content with high precision.

## 🚀 Key Features
- **Automated Classification:** Detects sophisticated phishing patterns in email bodies and headers.
- **Explainable AI (XAI):** Provides transparency by highlighting specific triggers that lead to a "Phishing" classification.
- **Modular Backend:** A Python-based inference engine that can be called by various frontends.

## 📊 Dataset & Training
The model was trained and evaluated on a combined corpus of **25,000+ emails** sourced from **Kaggle** and public security repositories. 
- **Preprocessing:** Involved tokenization, stop-word removal, and cleaning of raw email HTML/headers.
- **Model:** Fine-tuned **XLM-RoBERTa** for robust text feature extraction.

## 🛠 Tech Stack
- **AI/ML:** Python, PyTorch, HuggingFace, Scikit-learn
- **Interface:** JavaScript (Chrome Extension UI for email submission)
- **Backend:** Python (FastAPI/Flask)

## 📁 Repository Structure
- `backend/`: AI model logic and API endpoints.
- `extension/`: The user interface for interacting with the detection engine.
- `shared/`: Utility scripts and configuration.
- `storage/`: Data logs and local storage handling.
