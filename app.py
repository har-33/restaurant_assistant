from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

# ✅ MongoDB Atlas connection
client = MongoClient("mongodb+srv://harshad:harshad21@cluster0.nn5pcvb.mongodb.net/")
db = client["restaurant_db"]
orders = db["orders"]

# ✅ Serve the web UI
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    data = list(orders.find({}, {"_id": 0}))
    return jsonify(data)

# ✅ Add a new order
@app.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    if not data:
        return {"error": "No data provided"}, 400
    orders.insert_one(data)
    return {"message": "Order added successfully!"}

if __name__ == "__main__":
    app.run(debug=True)
