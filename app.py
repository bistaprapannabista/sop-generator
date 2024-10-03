import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

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

st.set_page_config(layout="wide") 

st.title("🤖 SOP Generator: Your own AI to write SOP. ✍️")

st.subheader("Now you don't need to write sop manually. Welcome to the AI era.")

with st.sidebar:
    st.title("Enter Details here")

    life_aim = st.text_input(label="Aim in life")

    destination_country = st.selectbox(label="Destination Country",options=["Japan", "USA"])

    qualification = st.selectbox(label="Qualification",options=["+2","Bachelors","Masters"])

    studied_subjects = st.text_area(label="Studied Subjects")

    no_of_words = st.slider(label="Number of Words",step=50,min_value=100,max_value=1000)

    submit_button = st.button(label="Generate")


if submit_button:
    prompt = f"Write a clear and concise {no_of_words}-word statement of purpose for a student from Nepal who has completed {qualification} education, focusing on subjects such as {studied_subjects}. The student is applying to study in {destination_country}. Include details about their academic background, their interest in {destination_country}'s education system, and their curiosity about its culture. Emphasize the student's goals to contribute to society through their education and experience gained in {destination_country}, as well as how this aligns with their life aim: {life_aim}. Use simple language and easy-to-understand vocabulary, as English is not the student's native language."
    # response = ollama.chat(model='llama3.2', messages=[{
    #     'role': 'user',
    #     'content': prompt},])
    # output = response['message']['content']
    output = chat_session.send_message(prompt)
    st.text(output.text)
    st.download_button("Click here to download", output.text)


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
    