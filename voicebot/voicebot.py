import os
import json
import requests
import speech_recognition as sr
import pyttsx3

API_ENDPOINT = os.environ.get("CHAT_API_ENDPOINT", "http://localhost:8000/chat")


def recognize_speech(recognizer, microphone):
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("You:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Speech recognition error:", e)
    return None


def generate_response(message, history):
    payload = {"message": message, "conversationHistory": history}
    try:
        res = requests.post(API_ENDPOINT, json=payload)
        res.raise_for_status()
        data = res.json()
        if data.get("success"):
            return data.get("response", "")
    except Exception as e:
        print("API error:", e)
    return "Sorry, I couldn't process that."


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    history = []
    print("Start a conversation. Press Ctrl+C to exit.")
    try:
        while True:
            text = recognize_speech(recognizer, mic)
            if not text:
                continue
            history.append({"role": "user", "content": text})
            response = generate_response(text, history)
            print("Bot:", response)
            history.append({"role": "assistant", "content": response})
            speak_text(response)
    except KeyboardInterrupt:
        print("Goodbye!")


if __name__ == "__main__":
    main()
