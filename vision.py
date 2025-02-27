from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai
from PIL import Image

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response from Gemini
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])  # Check method name
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit UI setup
st.set_page_config(page_title="Gemini Image Classifier")
st.header("Gemini Image Classifier")

input = st.text_input("Input prompt: ", key="input")

uploaded_file=st.file_uploader("Choose an image ",type=["jpg","jpeg","png"])
imag=""

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="uploaded image",use_column_width=True)

submit=st.button("Describe the image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("the response is")
    st.write(response)