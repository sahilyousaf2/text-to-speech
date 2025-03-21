import pyttsx3;
import streamlit as st;
engine = pyttsx3.init()



st.title("Text To Speech");


text = st.text_area("Enter your text here");
if st.button("Speech"):
    engine.say(text);
    engine.runAndWait();
    engine.setProperty('rate', 150)