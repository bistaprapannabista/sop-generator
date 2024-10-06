import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
# from textblob import TextBlob
import random

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

# def humanize_text(text):
#     blob = TextBlob(text)
#     # You can add more complex processing here
#     return str(blob.correct())  # Returns corrected text


st.set_page_config(page_title="SOP Generator",page_icon="✍️",layout="wide",initial_sidebar_state="expanded") 

st.title("🤖 SOP Generator: Your own AI to write SOP. ✍️")

st.subheader("Now you don't need to write sop manually. Welcome to the AI era.")

with st.sidebar:
    st.title("Enter Details here")

    life_aim = st.text_input(label="Aim in life")

    currently_busy_on = st.text_input(label="Currently Busy on")

    destination_country = st.selectbox(label="Destination Country",options=["Japan", "USA"])

    qualification = st.selectbox(label="Qualification",options=["+2","Bachelors","Masters"])

    studied_subjects = st.text_area(label="Studied Subjects")

    no_of_words = st.slider(label="Number of Words",step=50,min_value=100,max_value=1000)

    submit_button = st.button(label="Generate")


if submit_button:
    prompt = f"Write a {no_of_words}-word Statement of Purpose (SOP) for a Nepali student who has completed {qualification} and is currently engaged in {currently_busy_on}. The student has a background in {studied_subjects} and is applying to study in {destination_country}. Highlight their academic journey, specific reasons for choosing the education system of {destination_country}, and their appreciation for its culture. Explain how the knowledge and experiences gained will help them contribute to society, aligning with their personal goal of {life_aim}. Use clear, simple language suitable for a non-native English speaker, avoiding the mention of any specific university or student name."
    # response = ollama.chat(model='llama3.2', messages=[{
    #     'role': 'user',
    #     'content': prompt},])
    # output = response['message']['content']
    response = chat_session.send_message(prompt)
    # output = text = Humanizer.humanize(response.text)
    output = response.text
    # st.text(output)
    st.code(output)
    st.download_button("Click here to download", output)


footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: lightgray;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        <p>Developed by Prapanna Bista | © 2024 All rights reserved</p>
    </div>
    """
st.markdown(footer, unsafe_allow_html=True)
    