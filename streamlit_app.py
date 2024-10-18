import streamlit as st
from transformers import pipeline

### Create a GPT2 generator pipeline
generator = pipeline("text-generation", model="gpt2")

prompt = st.text_input("🎈 What is your prompt today?")
length= st.number_input(
    "The expected length of the response", value=20, placeholder="Type a number..."
)


### Generate the answer to the question
st.header("🎈 High level of creativity response")
st.write(
generator(prompt, max_length=length, do_sample=False, truncation=True)[0]["generated_text"]
)

st.header("🎈 Predictable response")
st.write(
generator(prompt, max_length=length, temperature=0, truncation=True)[0]["generated_text"]
)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
