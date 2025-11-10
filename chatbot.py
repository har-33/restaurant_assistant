def chatbot_reply(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Hello! Welcome to Sainath’s Restaurant Assistant. How may I help you today?"

    elif "menu" in text:
        return (
            "Here’s our popular menu for today:\n"
            "- Cheese Pizza\n"
            "- Veg Burger\n"
            "- French Fries\n"
            "- Coke\n"
            "Would you like to place an order?"
        )

    elif "cheese pizza" in text:
        return "Cheese Pizza added to your order! Would you like to add a drink or side?"

    elif "veg burger" in text:
        return "Veg Burger added! Want to make it a combo with fries and coke?"

    elif "french fries" in text:
        return "Crispy french fries added! Want a drink too?"

    elif "cold drinks" in text:
        return "Cold-drinks added! Should I confirm your order?"

    elif "order" in text or "confirm" in text:
        return "Your order has been placed successfully! Thank you for choosing Sainath’s Restaurant."

    elif "bye" in text:
        return "Goodbye! Have a delicious day ahead visit again sainath restaurant!"

    else:
        return "I didn’t quite catch that. Could you please rephrase?"
