# This is a lanchain python project for linkdin search
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field   
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
tavily = TavilyClient()
@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

class JobPosting(BaseModel):
    title: str
    company: str
    location: str
    url: str    

class JobSearchResult(BaseModel):
    postings: list[JobPosting]

llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm,tools=tools,response_format=JobSearchResult)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the vancouver area on linkedin and list their details")})
    print(result)
if __name__ == "__main__":
    main()