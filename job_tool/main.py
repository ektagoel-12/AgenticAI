import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text,extract_resume_text
import tempfile
import os

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧Job Outreach Tool r")

    # Step 1: Upload Resume
    st.header("Upload your Resume(PDF)")
    resume_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

    st.subheader("🌐 Optional Links")
    portfolio_link = st.text_input("Portfolio Website (optional)")
    github_link = st.text_input("GitHub Profile (optional)")
    linkedin_link = st.text_input("LinkedIn Profile (optional)")

    st.subheader("📌 Job Posting")
    url_input = st.text_input("Enter a Job Post URL:")

    col1, col2 = st.columns(2)
    cold_email_btn = col1.button("Generate Cold Email")
    cover_letter_btn = col2.button("Generate Cover Letter")
    
    if resume_file:
        resume_text = extract_resume_text(resume_file)
        full_text = resume_text
        full_resume_text = resume_text
        # Append optional info to resume text
        optional_links = ""
        if portfolio_link:
            optional_links += f"Portfolio: {portfolio_link}\n"
        if github_link:
            optional_links += f"GitHub: {github_link}\n"
        if linkedin_link:
            optional_links += f"LinkedIn: {linkedin_link}\n"

        if optional_links:
            full_text += "\n\n" + optional_links

        portfolio.load_portfolio_from_resume(full_text)

    if cold_email_btn or cover_letter_btn:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            jobs = llm.extract_jobs(data)
            import json

            parsed_jobs = []
            for j in jobs:
                if hasattr(j, 'content'):  # if it's an AIMessage
                    try:
                        parsed_jobs.append(json.loads(j.content))
                    except Exception as e:
                        st.error(f"Could not parse job description: {e}")
                else:
                    parsed_jobs.append(j)  # fallback
            for job in parsed_jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)

                if cold_email_btn:
                    email = llm.write_mail(job, links, resume_text=full_resume_text)
                    st.subheader("📧 Cold Email")
                    st.code(email, language='markdown')
                elif cover_letter_btn:
                    cover_letter = llm.write_cover_letter(job, links, resume_text=full_resume_text)
                    st.subheader("📄 Cover Letter")
                    st.code(cover_letter, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Job Outreach Tool", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

