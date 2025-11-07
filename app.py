from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://harshad:harshad21@cluster0.nn5pcvb.mongodb.net/")
db = client["restaurant_db"]
orders = db["orders"]

@app.route("/")
def home():
    return {"message": "Welcome to Restaurant API!"}

@app.route("/orders", methods=["GET"])
def get_orders():
    data = list(orders.find({}, {"_id": 0}))
    return jsonify(data)

@app.route("/orders", methods=["POST"])
def add_order():
    data = request.json
    orders.insert_one(data)
    return {"message": "Order added successfully!"}

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()

    # Simple menu list
    menu_items = ["pizza", "burger", "fries", "coffee", "cold drink"]

    # 🍕 ORDER intent
    if "order" in user_msg or "want" in user_msg or "give me" in user_msg:
        found_item = None
        for item in menu_items:
            if item in user_msg:
                found_item = item
                break

        if found_item:
            order = {"customer": "Guest", "item": found_item.title(), "price": 299}
            orders.insert_one(order)
            reply = f"✅ Your {found_item} order has been placed successfully!"
        else:
            reply = "I heard you want to order something, but can you say the item name?"

    # 📋 SHOW ORDERS intent
    elif "show" in user_msg and "order" in user_msg or "my orders" in user_msg:
        recent_orders = list(orders.find({}, {"_id": 0}).sort("_id", -1).limit(3))
        if not recent_orders:
            reply = "You have no orders yet."
        else:
            summary = ", ".join([o["item"] for o in recent_orders])
            reply = f"Here are your latest orders: {summary}."
    
    # 🍽 MENU intent
    elif "menu" in user_msg:
        reply = "We have pizza, burgers, fries, coffee, and cold drinks."
    
    # 🙋 GREETING
    elif "hello" in user_msg or "hi" in user_msg:
        reply = "Hello! Welcome to Domino's assistant. What would you like to order today?"
    
    # 🙏 THANKS
    elif "thanks" in user_msg:
        reply = "You're welcome!"
    
    # 👋 BYE
    elif "bye" in user_msg:
        reply = "Goodbye! Have a great day!"
    
    # 🤔 Unknown
    else:
        reply = "Hmm, I’m not sure about that."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
