import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm=ChatGroq(
            model="llama3-70b-8192",
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
    def extract_jobs(self,cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE
            {page_data}

            ### INSTRUCTION
            The scraped text is from a careers page.
            Extract all job postings and return them **only** in **valid JSON format** using the following keys: `role`, `experience`, `skills`, and `description`.

            Do **not** include any explanation, heading, or preamble.  
            Do **not** wrap the JSON in triple backticks.  
            Do **not** say anything like "Here's the result" or "Below is the JSON".

            Just return **pure JSON**, beginning with `{{` and ending with `}}`.

            ### OUTPUT:
            """

            )

        chain_extract= prompt_extract | self.llm
        res=chain_extract.invoke(input={'page_data': cleaned_text})
        try:
            json_parser=JsonOutputParser()
        except OutputParserException:
            raise OutputParserException("Context too big,unable to parse jobs.")
        return res if isinstance(res,list) else [res]
    
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Ekta Goel, a final-year Integrated M.Tech student specializing in Computer Science and Engineering, currently interning at Intel Corporation as a Data Engineering and MLOps Intern. 

            You are writing a cold email expressing interest in the role described above. Highlight your hands-on experience in:

            - Building enterprise-grade CI/CD MLOps pipelines using Streamlit, GitHub Actions, and Databricks CLI.
            - Automating data quality checks with Snowflake and Python (1M+ records), reducing manual work by 70%.
            - Developing LLM-based data extraction pipelines using LangChain and Trafilatura.
            - Constructing end-to-end ML/NLP pipelines using Whisper ASR and BERT, achieving 95.4% accuracy.
            - Creating scalable ingestion and transformation pipelines with Azure Data Factory, Snowflake, and Databricks.
            - Engineering real-time monitoring tools and approval portals using PowerApps, MongoDB, Flask, and REST APIs.

            Also include links to relevant projects and portfolios that showcase your capability:
            - GitHub Webhook Monitoring System: https://github.com/ektagoel-12/webhook-repo  
            - Audio-to-Text Punctuation Prediction: https://github.com/ektagoel-12/Python-Projects/tree/main/Audio_to_test_punctuation_prediction  
            - Personal Portfolio: https://ektagoel.site/

            Write a concise, professional cold email tailored to the job description. You are not representing any company—just showcasing your individual capabilities and interest in the position.

            ### EMAIL (NO PREAMBLE):
            
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))

