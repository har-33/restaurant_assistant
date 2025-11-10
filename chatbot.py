import pyttsx3
import speech_recognition as sr

# 🎙️ Text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # [0] for male, [1] for female (you can change)
    engine.say(text)
    engine.runAndWait()

# 🎧 Speech-to-text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now.")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("🤖 Bot: Sorry, I didn’t catch that.")
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        print("⚠️ Could not connect to speech recognition service.")
        return ""

# 💬 Chatbot logic
def chatbot_reply(text):
    text = text.lower()
    if "hello" in text or "hi" in text:
        return "Hello regumsoft! Welcome to sainath virtual assistant. How may I assist you today?"
    
    elif "menu" in text:
        return (
            "Certainly! Here’s our popular menu for today:\n"
            "- Cheese Pizza\n"
            "- Veg Burger\n"
            "- french Fries\n"
            "- Coca-cola\n"
            "Would you like me to place an order for you?"
        )
    
    elif "cheese pizza" in text:
        return "Got it! One Cheese Pizza added to your order. Would you like to add any drinks or sides with that?"
    
    elif "veg burger" in text:
        return "Great choice! Veg Burger added to your order. Would you like to make it a combo with fries and coke?"
    
    elif "french fries" in text:
        return "Crispy French Fries added to your cart! Would you like to add a drink as well?"
    
    elif "coca-cola" in text:
        return "Cool choice! Coca-cola added. Would you like to confirm your order now?"
    
    elif "order" in text:
        return "Sure! Please mention the item name and quantity you’d like to order."
    
    elif "confirm" in text:
        return "Your order has been placed successfully. It will be ready for delivery shortly. Thank you for choosing Domino’s!"
    
    elif "bye" in text or "exit" in text:
        return "Goodbye! Thank you for visiting Domino’s. Have a delicious day ahead!"
    
    else:
        return ("Hi")
