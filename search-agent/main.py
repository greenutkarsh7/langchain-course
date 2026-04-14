from typing import List
from dotenv import load_dotenv
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
    Tool that searches over internet.
    Args:
        query: The query to search for.
    Returns:
        The search result.
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm=ChatOpenAI(model="gpt-5")
tools=[search]
agent=create_agent(model=llm, tools=tools)


def main():
    print("Hello from search-agent!")
    result = agent.invoke({
        "messages": [HumanMessage(content="What is the stock price of amazon?")]
        })
    print("------Final Output-------")    
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
