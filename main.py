import pyttsx3
import streamlit as st

# Initialize the TTS engine globally
engine = pyttsx3.init()

# Set up Streamlit UI
st.title("Text To Speech")

# Input text area
text = st.text_area("Enter your text here")

# Button to trigger speech
if st.button("Speech"):
    # Set voice properties for better pronunciation
    voices = engine.getProperty('voices')
    
    # Use a better voice (if available)
    for voice in voices:
        if "english" in voice.name.lower():  # Change to "hindi" if Hindi voice is available
            engine.setProperty('voice', voice.id)
            break
    
    # Adjust speech rate (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

# Button to stop speech
if st.button("Stop"):
    engine.stop()
    st.write("Speech stopped.")