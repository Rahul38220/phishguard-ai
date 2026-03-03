# PhishGuard AI: Multilingual Phishing Detection Framework
**Lead Researcher & Developer** | Published in IRJET, 2025

## 📌 Overview
[cite_start]PhishGuard AI is an AI-powered cybersecurity system that detects phishing attempts using **XLM-RoBERTa** and generates human-readable explanations via **mT5**[cite: 23, 26]. [cite_start]The project consists of a high-performance **FastAPI** backend and a **Chrome Extension** frontend designed to improve digital literacy for users by explaining *why* an email was flagged[cite: 24, 29].

## 🚀 Key Results
[cite_start]In comparative testing against other transformer models, PhishGuard AI (XLM-RoBERTa) achieved superior performance[cite: 218, 239]:
* [cite_start]**Accuracy:** 97.23% 
* [cite_start]**Precision (Phishing):** 0.94 
* [cite_start]**Recall (Phishing):** 0.93 
* [cite_start]**ROC-AUC Score:** 0.98 

## 🛠 Methodology & Tech Stack
- [cite_start]**Models:** Fine-tuned **XLM-RoBERTa-base** for classification and **mT5-small** for multilingual explanation generation[cite: 58].
- [cite_start]**Backend:** **FastAPI** (Python) for scalable AI inference and Pydantic for data integrity.
- [cite_start]**Frontend:** **Chrome Extension** (JavaScript) for real-time user interaction and email submission[cite: 73, 76].
- [cite_start]**Dataset:** A curated corpus of **23,766 messages** sourced from the SMS Spam Collection and Phishing Email datasets on Kaggle[cite: 94, 112].

## 📁 Repository Structure
- [cite_start]`backend/`: FastAPI server and model inference logic[cite: 67].
- [cite_start]`extension/`: Chrome Extension frontend and background scripts[cite: 73].
- [cite_start]`research/`: Contains the full published research paper[cite: 54].

## 📄 Publication
**"PhishGuard AI: A Framework for Multilingual Phishing Detection using XLM-ROBERTa & mT5"**
Published in the *International Research Journal of Engineering and Technology (IRJET)*, Volume 12, Issue 10, Oct 2025.
[cite_start][Read the full paper here](https://www.irjet.net/archives/V12/i10/IRJET-V12I1063.pdf)[cite: 1, 12].
