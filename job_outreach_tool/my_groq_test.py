from langchain_groq import ChatGroq
import os
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
#     max_tokens=None,
    groq_api_key=os.getenv("GROQ_API_KEY")
    # other params...
)

response=llm.invoke("The first person to land on moon was...")
print(response.content)