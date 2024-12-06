import streamlit as st
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
import os


OPENAI_API_KEY = st.secrets["OpenAIkey"]


question = st.text_input


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"), # To be used by the agent for intermediate operations.
    ]
)

chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4o-mini")

# Setting up the Serper tool
os.environ["SERPER_API_KEY"] = st.secrets['SERPER_API']
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="GoogleSerper",
        func=search.run,
        description="Useful for when you need to look up some information on the internet.",
    )
]

question

# Defining the agent
agent = create_tool_calling_agent(chat, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) #, verbose=True

st.write("Vanilla LLM answer:", chat(question).content)

# Run the agent
st.write("*****")
st.write("Agent answer:", agent_executor.invoke({"input": question})["output"])
