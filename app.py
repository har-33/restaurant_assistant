from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Atlas connection string
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient("mongodb+srv://harshad:<harshad21>@test.l765a1d.mongodb.net/")
db = client["restaurant_db"]
orders = db["orders"]

@app.route('/')
def home():
    return {"message": "Welcome to Restaurant API!"}

@app.route('/orders', methods=['GET'])
def get_orders():
    data = list(orders.find({}, {"_id": 0}))
    return jsonify(data)

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    orders.insert_one(data)
    return {"message": "Order added successfully!"}

if __name__ == "__main__":
    app.run(debug=True)
