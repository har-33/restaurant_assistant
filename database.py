from pymongo import MongoClient
import os

# ✅ Environment variable support for Render
MONGO_URI = os.getenv("mongodb+srv://harshad:harshad21@cluster0.nn5pcvb.mongodb.net/")

client = MongoClient(MONGO_URI)
db = client["restaurant_db"]
orders_collection = db["orders"]
