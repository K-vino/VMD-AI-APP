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
 
