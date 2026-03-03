# PhishGuard AI: Multilingual Phishing Detection Framework
**Lead Researcher & Developer** | Published in IRJET (Oct 2025)

## 📌 Overview
PhishGuard AI is an end-to-end cybersecurity solution featuring a Chrome Extension and a localized backend. It detects phishing attempts in English, Hindi, and Gujarati, providing real-time protection and digital literacy for non-native English speakers.

## 🚀 Key Features
- **Chrome Extension Integration:** Real-time scanning of browser content.
- **Multilingual NLP:** Uses XLM-RoBERTa to analyze code-switching and regional dialects.
- **Explainable AI:** Breaks down *why* a site is dangerous in the user's native language.

## 📊 Dataset & Training
The model was trained and validated using a combined corpus of approximately **25,000+ emails and URLs**, integrating both public security datasets and curated multilingual samples to ensure high accuracy across diverse linguistic patterns.

## 🛠 Tech Stack
- **AI/ML:** Python, PyTorch, XLM-RoBERTa
- **Frontend:** JavaScript (Chrome Extension API)
- **Backend:** Python (FastAPI/Flask)

## 📁 Repository Structure
- `backend/`: AI model API and detection logic.
- `extension/`: Chrome Extension frontend and manifest files.
- `shared/`: Common utilities and multilingual dictionaries.
- `storage/`: Localized data handling and logs.
- `run.sh`: Automated script to boot the environment.

## 📄 Research & Publication
Published in the *International Research Journal of Engineering and Technology (IRJET)*, Volume 12, Issue 10.
