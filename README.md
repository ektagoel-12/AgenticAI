# AgenticAI

A collection of small LLM and agent experiments: a finance research agent, a PDF Q&A assistant, a video summarizer and a job outreach generator.

## Projects

| Folder | What it is | Main tools |
|---|---|---|
| `financial_analyst/` | Agents that search the web and pull stock prices, analyst recommendations, company info and news. `playground.py` serves them for chat. | phidata, Groq (llama3-70b), yfinance, DuckDuckGo |
| `pdf_assistant/` | CLI assistant that answers questions over a PDF (Thai recipes sample) with hybrid vector search and stored chat history. | phidata, Groq, PgVector, Typer |
| `Video Summarizer/` | Streamlit app intended to summarize uploaded video with Gemini. Work in progress: `app.py` has syntax errors to fix before it runs. | Streamlit, Gemini, phidata |
| `job_tool/` | Streamlit app that writes cold emails from a job posting, matched against a portfolio in ChromaDB. Has its own [README](job_tool/README.md). | LangChain, ChromaDB, Streamlit |
| `job_outreach_tool/` | Extended version of `job_tool`: resume PDF upload, cold email and cover letter generation. | LangChain, ChromaDB, Streamlit |

## Setup

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`job_tool/` and `job_outreach_tool/` have their own `requirements.txt`.

Create a `.env` in the folder you run from with the keys that project needs:

| Variable | Used by |
|---|---|
| `GROQ_API_KEY` | `financial_analyst`, `pdf_assistant` |
| `OPENAI_API_KEY` | `financial_analyst` |
| `GOOGLE_API_KEY` | `Video Summarizer` |
| `FIREWORKS_API_KEY` | `job_tool`, `job_outreach_tool` (see their README) |

## Running

```bash
python financial_analyst/financial_agent.py
python financial_analyst/playground.py
python pdf_assistant/pdf_assistant.py        # needs Postgres with pgvector on localhost:5532
streamlit run job_outreach_tool/main.py
```

## Notes

- The sample `my_portfolio.csv` files contain placeholder example links.
- Chroma vector store folders are committed to the repo; they are generated data and can be rebuilt.
