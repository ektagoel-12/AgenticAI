import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file,get_file
import generativeai as genai

import time
from pathlib import Path
import tempfile

from dotenv import load_dotenv
load_dotenv()

import os

API_KEY=os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

#PAGE CONFIGURATION
st.set_page_config(
    page_title=="Multimodal AI Agent- Video Summarizer",
    page_icon==" ",
    layout=="wide"
)

st.title("Phidata Video AI Summarizer Agent")
st.header("Powered by Gemini 2.0 Flash Exp")

@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.5-flash")
        tools=[DuckDuckGo()],
        markdown=True
    )

multimodal_Agent=st.file_uploader(
    "Upload a video file",type=['mp4','mov','avi'],help="Upload a video for AI analytics"
)