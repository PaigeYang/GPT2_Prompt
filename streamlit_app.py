import streamlit as st
from transformers import pipeline

### Create a GPT2 generator pipeline
generator = pipeline("text-generation", model="gpt2")

st.title("🎈My IS883 Week6 Assignment")

prompt = st.text_input("What is your prompt today?")
length= st.number_input(
    "The expected length of the response", value=20, placeholder="Type a number..."
)

### Generate the answer to the question
### Set temperature as 100 for high level of creativity response
st.header("High level of creativity response")
st.write(
generator(prompt, max_length=length, temperature=100.0, truncation=True)[0]["generated_text"]
)

### Set temperature as 0.1 for predictable response
st.header("Predictable response")
st.write(
generator(prompt, max_length=length, temperature=0.1, truncation=True)[0]["generated_text"]
)
