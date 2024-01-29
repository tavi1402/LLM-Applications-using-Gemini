from dotenv import load_dotenv
load_dotenv()

import os 
import streamlit as st
import google.generativeai as genai


#KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#MODEL
model= genai.GenerativeModel("gemini-pro")

def genrate_response(input):
    response= model.generate_content(input)
    return response.text

st.set_page_config(
    page_title="My Awesome Gemini App",
    page_icon="🚀")

st.header("Gemini basic App")

input= st.text_input("Inputt :", key="input")
submit= st.button("Ask you query here")

if submit:
    response= genrate_response(input)
    st.subheader("The Response is ")
    st.write(response)

