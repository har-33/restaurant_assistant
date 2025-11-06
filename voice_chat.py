import speech_recognition as sr
import pyttsx3
from pymongo import MongoClient
import time

# --------------------------
# MongoDB Setup
# --------------------------
client = MongoClient("mongodb+srv://harshad:harshad21@test.l765a1d.mongodb.net/")
db = client["restaurant_db"]
orders = db["orders"]

# --------------------------
# Speak Function (male voice)
# --------------------------
def speak(text):
    print(f"🤖 Bot: {text}")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for v in voices:
        if "male" in v.name.lower() or "david" in v.name.lower():
            engine.setProperty('voice', v.id)
            break
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

# --------------------------
# Listen Function
# --------------------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=8, phrase_time_limit=10)
    try:
        query = r.recognize_google(audio)
        print(f"🗣️ You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

# --------------------------
# Chatbot Logic + MongoDB
# --------------------------
def chatbot_logic(text):
    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to Domino's assistant. What would you like to order?"

    elif "menu" in text:
        return "We have pizza, burger, fries, and coke. What do you want?"

    elif "pizza" in text:
        order = {"customer": "VoiceUser", "item": "Pizza", "price": 299}
        orders.insert_one(order)
        return "Pizza order placed successfully!"

    elif "burger" in text:
        order = {"customer": "VoiceUser", "item": "Burger", "price": 199}
        orders.insert_one(order)
        return "Burger order placed successfully!"

    elif "fries" in text:
        order = {"customer": "VoiceUser", "item": "fries", "price": 99}
        orders.insert_one(order)
        return "fries order placed successfully!"

    elif "coke" in text:
        order = {"customer": "VoiceUser", "item": "coke", "price": 49}
        orders.insert_one(order)
        return "coke order placed successfully!"
    
    elif "thanks" in text or "thank you" in text:
        return "You're welcome! Enjoy your meal!"

    elif "bye" in text:
        return "Goodbye! Have a great day!"

    else:
        return "Hmm, I didn’t understand. Could you say that again?"

# --------------------------
# Main Loop
# --------------------------
def main():
    speak("Hello! I am your domino's assistant. How can I help you today?")
    while True:
        user_input = listen()
        if user_input:
            reply = chatbot_logic(user_input)
            speak(reply)
            if "bye" in user_input:
                break
        time.sleep(0.5)

if __name__ == "__main__":
    main()
