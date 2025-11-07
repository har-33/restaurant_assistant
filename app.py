from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# MongoDB connection
client = MongoClient("mongodb+srv://harshad:harshad21@test.l765a1d.mongodb.net/")
db = client["restaurant_db"]
orders = db["orders"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/orders', methods=['GET'])
def get_orders():
    data = list(orders.find({}, {"_id": 0}))
    return jsonify(data)

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    orders.insert_one(data)
    return jsonify({"message": "Order added successfully!"})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").lower()

    if "hello" in user_input or "hi" in user_input:
        return jsonify({"reply": "Hello! How can I help you today?"})
    elif "menu" in user_input:
        return jsonify({"reply": "We have pizza, burgers, fries, and cold drinks."})
    elif "pizza" in user_input:
        return jsonify({"reply": "Great choice! Our cheese pizza is the best seller."})
    elif "bye" in user_input:
        return jsonify({"reply": "Goodbye! Have a great day!"})
    else:
        return jsonify({"reply": "Sorry, I didn’t quite get that. Could you repeat?"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
