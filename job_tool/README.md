# 📧 Cold Outreach Generator for Job Seekers

An LLM-powered job outreach system that enables individuals to create hyper-personalized cold emails and cover letters for job applications, using only their resume and optional GitHub, Portfolio, and LinkedIn URLs.

## 🚀 Features

- 🧠 **Generative AI with LLM (LLaMA 4 via Fireworks API)**
- 📄 **Resume Upload (PDF) + Automatic Parsing**
- 🌐 **Web Scraping for GitHub & Portfolio**
- 🧭 **Vector Database Matching (ChromaDB)**: Ranks your work against the job description
- 📨 **Cold Email & Cover Letter Generator**: Generates either or both at once
- 💡 **Non-destructive Output**: Cold email and cover letter are stored and shown independently
- ✨ **No Templates**: Fully personalized using LangChain + Chroma + Fireworks API

## 🏗️ Architecture

- **Frontend**: Streamlit (UI)
- **LLM**: Meta LLaMA 4 (via Fireworks.ai API)
- **Embedding & Retrieval**: ChromaDB + LangChain
- **PDF Parsing**: PyMuPDF
- **Web Scraping**: LangChain `WebBaseLoader`

## 📦 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/job-outreach-tool.git
   cd job-outreach-tool
   
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt

3. Create .env with your Fireworks API key:
   ```env
   FIREWORKS_API_KEY=your_actual_key
4. Run the app:
   ```bash
   streamlit run main.py
