import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chatbot import chatbot_reply
from database import orders_collection

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Set correct absolute paths (important for Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# ✅ Homepage
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ Menu API
@app.get("/menu")
async def get_menu():
    menu = [
        {"item": "Cheese Pizza", "price": 299},
        {"item": "Veg Burger", "price": 199},
        {"item": "French Fries", "price": 99},
        {"item": "Coke", "price": 49},
    ]
    return {"menu": menu}

# ✅ Order API
@app.post("/order")
async def place_order(order: dict):
    orders_collection.insert_one(order)
    return {"message": "Order placed successfully!"}

# ✅ Chatbot API
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    reply = chatbot_reply(user_message)
    return JSONResponse({"reply": reply})

# ✅ Health Check (Render debug)
@app.get("/ping")
async def ping():
    return {"status": "ok"}

# ✅ Local run only (Render ignores this)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
