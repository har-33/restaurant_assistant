from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chatbot import chatbot_reply
from database import orders_collection

app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/menu")
async def get_menu():
    menu = [
        {"item": "Cheese Pizza", "price": 299},
        {"item": "Veg Burger", "price": 199},
        {"item": "French Fries", "price": 99},
        {"item": "Coke", "price": 49}
    ]
    return {"menu": menu}

@app.post("/order")
async def place_order(order: dict):
    orders_collection.insert_one(order)
    return {"message": "Order placed successfully!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    reply = chatbot_reply(user_message)
    return JSONResponse({"reply": reply})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
