from dotenv import load_dotenv
load_dotenv()
import os 
import streamlit as st
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model= genai.GenerativeModel("gemini-pro")

chat= model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Auention and Answer App")
st.header("Gemini Application of Question and Answer")

input= st.text_input("input: ", key= "input")
submit= st.button("Ask Youu Question here")

if submit:
    response= get_gemini_response(input)
    st.subheader("The response is ...")
    for chunk in response:
        print(st.write(chunk.text))
        print("#"* 100)
    
    st.write(chat.history)