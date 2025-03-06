from fastapi import FastAPI
import requests

app = FastAPI()
SERVICE_B_URL = "http://service_b:8001/items"

@app.get("/items/{item_id}")
def get_item(item_id: int):
    response = requests.get(f"{SERVICE_B_URL}/{item_id}")
    return response.json()

@app.post("/items/")
def create_item(item: dict):
    response = requests.post(SERVICE_B_URL, json=item)
    return response.json()
