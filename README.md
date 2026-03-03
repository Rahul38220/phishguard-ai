# PhishGuard AI: Multilingual Phishing Detection Framework
**Lead Researcher & Developer** | Published in IRJET, 2025

## 📌 Overview
PhishGuard AI is an AI-powered cybersecurity system that detects phishing attempts using **XLM-RoBERTa** and generates human-readable explanations via **mT5**. The project features a high-performance **FastAPI** backend and a **Chrome Extension** frontend designed to improve digital literacy by explaining the "rationale" behind a classification.

## 🚀 Key Results
In comparative testing against other transformer models, PhishGuard AI (XLM-RoBERTa) achieved superior performance:
* **Accuracy:** 97.23%
* **Precision (Phishing):** 0.94
* **Recall (Phishing):** 0.93
* **ROC-AUC Score:** 0.98

## 🛠 Methodology & Tech Stack
- **Models:** Fine-tuned **XLM-RoBERTa-base** for classification and **mT5-small** for multilingual explanation generation.
- **Backend:** **FastAPI** (Python) for scalable AI inference and **Pydantic** for data integrity.
- **Frontend:** **Chrome Extension** (JavaScript) for real-time user interaction.
- **Dataset:** A curated corpus of **23,766 messages** sourced from the SMS Spam Collection and Phishing Email datasets on Kaggle.

## 📁 Repository Structure
- `backend/`: FastAPI server and model inference logic.
- `extension/`: Chrome Extension frontend and background scripts.
- `shared/`: Language detection utilities and global configurations.
- `storage/`: Localized storage for recording detected suspicious origins.
- `research/`: Contains the full published research paper.

## 📄 Publication
**"PhishGuard AI: A Framework for Multilingual Phishing Detection using XLM-ROBERTa & mT5"**
Published in the *International Research Journal of Engineering and Technology (IRJET)*, Volume 12, Issue 10, Oct 2025.

[Read the full paper here](https://www.irjet.net/archives/V12/i10/IRJET-V12I1063.pdf)
