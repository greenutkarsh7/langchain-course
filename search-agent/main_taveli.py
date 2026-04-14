from typing import List
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch, tavily_search


llm=ChatOpenAI(model="gpt-5")
tools=[TavilySearch()]
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
