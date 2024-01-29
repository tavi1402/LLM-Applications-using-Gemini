from dotenv import load_dotenv
load_dotenv()

import os 
import streamlit as st
import google.generativeai as genai
from PIL import Image


#KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#MODEL
model= genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input!= "":
        response= model.generate_content([input,image])
    else:
        response= model.generate_content(image)

    return response.text

st.set_page_config(page_title="LLM IAMGE APPLICATION")

st.header("LLM APPLICATION Image To Text using GEMINI")

input=st.text_input("Input",key= "input")

uploaded_file= st.file_uploader("Choose the image", type = ["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption= "uploaded image....", use_column_width=True)

submit= st.button("Tell me about the images")

if submit:
    response= get_gemini_response(input,image)
    st.subheader("The Response is......")
    st.write(response)
