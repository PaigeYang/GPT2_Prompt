import streamlit as st
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
import os


OPENAI_API_KEY = st.secrets["OpenAIkey"]


user_query = st.text_input("Which restaurant you are looking for?")

instruction = f"""
Based on the user's query, please search for detailed information on that place(s) in Boston.
1) Details to Provide:
- Name
- Address
- Website link (if available).
- Phone number
- Google rating
3. Analyze and summarize the overall sentiment from reviews.
Highlight the key strengths and potential drawbacks of the place. 
Recommend whether the location is suited for:
- Gatherings (consider factors like location, accessibility, seating, etc. for groups of friends or families)
- Dating (consider factors like atmosphere, cuisine, service quality, etc. for couples)
- Remote Working (consider factors like noise level, availability of outlets, Wi-Fi, etc.)

User query: {user_query}
"""

chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4o-mini")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"), # To be used by the agent for intermediate operations.
    ]
)



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

# Defining the agent
agent = create_tool_calling_agent(chat, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) #, verbose=True

if user_query:

    st.write("Vanilla LLM answer:", chat(instruction).content)
    
    # Run the agent
    st.write("*****")
    #st.write("Agent answer:", agent_executor.invoke({"input": question})["output"])
    
    st.write("Agent answer:", agent_executor.invoke({"input": instruction})["output"])
