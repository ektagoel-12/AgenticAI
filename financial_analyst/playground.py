import openai
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
from dotenv import load_dotenv
import os
import phi
from phi.playground import Playground,serve_playground_app
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")
## web search agent
web_search_agent=Agent(
    name="Web search Agent",
    role="Searchthe web for the information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-70b-8192"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)


app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)