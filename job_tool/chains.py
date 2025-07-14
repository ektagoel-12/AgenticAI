import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI


load_dotenv()

class Chain:
    def __init__(self):
        # self.llm=ChatGroq(
        self.llm=ChatOpenAI(
            # model="llama3-70b-8192",
            # temperature=0,
            # groq_api_key=os.getenv("GROQ_API_KEY")
            model="accounts/fireworks/models/llama4-maverick-instruct-basic",
            openai_api_base="https://api.fireworks.ai/inference/v1",
            openai_api_key=os.getenv("FIREWORKS_API_KEY"),
            temperature=0.6
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
    
    def write_mail(self, job, links,resume_text=""):
        prompt_email = PromptTemplate.from_template(
            """
            ### APPLICANT PROFILE:
            {resume_text}

            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are writing a cold email expressing interest in the role described above. Be concise and enthusiastic.
            Reference your resume content where applicable. Include any relevant portfolio links below:
            {link_list}

            ### COLD EMAIL:
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links, "resume_text": resume_text})
        return res.content
    
    def write_cover_letter(self, job, links,resume_text=""):
        prompt_cl = PromptTemplate.from_template(
            """
            ### APPLICANT PROFILE:
            {resume_text}

            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            Write a formal cover letter for this role. Tailor it using the applicant's profile above and include project links where relevant:
            {link_list}

            ### COVER LETTER:
            """
        )
        chain_cl = prompt_cl | self.llm
        res = chain_cl.invoke({"job_description": str(job), "link_list": links,"resume_text": resume_text})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))

