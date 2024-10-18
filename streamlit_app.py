import streamlit as st
from transformers import pipeline

### Create a GPT2 generator pipeline
generator = pipeline("text-generation", model="gpt2")

prompt = st.text_input("What is your prompt today?")
length= st.number_input(
    "The expected length of the response", value=20, placeholder="Type a number..."
)


### Generate the answer to the question "Damascus is a"
st.write(
generator(prompt, max_length=length, truncation=True)
)


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
