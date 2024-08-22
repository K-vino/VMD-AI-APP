import streamlit as st

st.title('WECOME TO MY AI WORLD')
st.header('I am Vino k')
st.image("./vino.png")
st.header('"Try my VMD AI..."')

import google.generativeai as genai
genai.configure(api_key="AIzaSyApxFggGSBX7ZrUukJFR4_AMpZj2SfmE6U")
text = st.text_input("Enter you question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if st.button("CLICK HERE"):
    response = chat.send_message(text)
    st.write(response.text)

import requests
import streamlit as st
import io
from PIL import Image

# Define API URL and headers
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

# Function to query the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit UI
st.title('Image Generator with Stable Diffusion')

# Text input for the prompt
prompt = st.text_input('Enter prompt:')

# Button to generate image
if st.button("Generate Image"):
    if prompt:
        # Query the API with the provided prompt
        image_bytes = query({"inputs": prompt})
        
        # Load and display the image
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption='Generated Image')
    else:
        st.warning('Please enter a prompt before clicking "Generate Image".')
 
 
