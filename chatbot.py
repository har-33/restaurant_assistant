#import pyttsx3
#import speech_recognition as sr

#◘def speak(text):
#    engine = pyttsx3.init()
#    engine.setProperty('rate', 170)
#    engine.say(text)
#    engine.runAndWait()

#def listen():
#   r = sr.Recognizer()
#   with sr.Microphone() as source:
#       print("🎤 Listening...")
#       r.adjust_for_ambient_noise(source)
#       audio = r.listen(source)
#   try:
#       return r.recognize_google(audio)
#   except:
#       return ""

def chatbot_reply(text):
    text = text.lower()
    if "hello" in text or "hi" in text:
        return "Hello! Welcome to Domino's Assistant. How can I help you?"
    elif "menu" in text:
        return "We have Cheese Pizza, Veg Burger, Fries, and Coke."
    elif "order" in text:
        return "Sure! Please tell me your item name and quantity."
    elif "bye" in text:
        return "Goodbye! Have a tasty day!"
    else:
        return "Sorry, I didn’t understand that. Could you repeat?"
