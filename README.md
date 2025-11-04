# 🍽️ Restaurant API (Flask + MongoDB Atlas)

A simple **Flask API** for managing restaurant orders, connected to **MongoDB Atlas (Cloud Database)**.  
This project is designed to help beginners understand how to:
- Build REST APIs with Flask  
- Store data in MongoDB Atlas  
- Deploy an app using Gunicorn (e.g., on Render, Railway, or Heroku)

---

## 🚀 Features

- 🧾 View all orders (`GET /orders`)
- ➕ Add new orders (`POST /orders`)
- ☁️ Cloud database using MongoDB Atlas
- 🔐 Environment variables handled securely using `.env`
- 🌐 Ready for deployment with **Gunicorn**

---

## 🏗️ Project Structure

restaurant_api/
│
├── app.py # Main Flask app file
├── requirements.txt # Dependencies
├── Procfile # Deployment config for Render/Heroku
├── .gitignore # Ignored files & folders
├── .env # MongoDB credentials (not uploaded)
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/restaurant-api.git
cd restaurant-api


### 2️⃣ Create a Virtual Environment

python -m venv .venv
.venv\Scripts\activate        # Windows
# OR
source .venv/bin/activate     # Mac/Linux

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Create .env File
Inside your project folder, create a file named .env:

MONGO_URI = "your_mongodb_atlas_connection_string"

### ▶️ Run the App Locally

python app.py

Open your browser and visit:
👉 http://127.0.0.1:5000

### 🌍 Deployment

🔹 Render (Recommended Free Hosting)

1. Push your code to GitHub

2. Create a new Web Service on Render

3. Connect your GitHub repo

4. Add environment variable:

MONGO_URI = your_connection_string

5. Render will auto-detect:

Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

### ✅ After deployment, you’ll get a public link like:
https://restaurant-api.onrender.com


### 🧾 License

This project is open source and free to use for learning purposes.

### 👨‍💻 Author

Harshad’s Restaurant API Project

Built with ❤️ using Flask, MongoDB Atlas, and Python.