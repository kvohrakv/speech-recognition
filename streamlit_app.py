import streamlit as st
import speech_recognition as sr
import pyaudio 
import pyperclip
import time 

def recognize_speech():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:
        st.write("Speak Anything:")
        
        # Adjusting for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Recording the audio using the microphone
        audio = recognizer.listen(source)
        
        try:
            # Using Google speech recognition with English language
            text = recognizer.recognize_google(audio, language="hi-IN")
            st.session_state["recognized_text"]=text
        except sr.UnknownValueError:
            st.error("Sorry, couldn't recognize what you said.")
        except sr.RequestError as e:
            st.error("Couldn't request results; {0}".format(e))

def main():
    st.title("Simple Speech Recognition App")
    st.write("Click on the 'Start Recording' button and speak into your microphone.")
    recognize_button = st.button("Start Recording")
    
    if recognize_button:
        recognize_speech()

    # Get the text to copy when the user clicks on the text area
    recognized_text = st.session_state.get("recognized_text")
    if recognized_text:
        st.text_area("Recognized Text:", recognized_text, key="recognized_text_area")
        copy_button = st.button("Copy", key="copy_button")
        if copy_button:
            # Clearing the clipboard first

            pyperclip.copy(recognized_text)
            st.write("Text copied to clipboard! You can now paste it elsewhere.")

if __name__ == "__main__":
    main()


