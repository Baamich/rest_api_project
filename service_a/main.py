from fastapi import FastAPI
import requests

app = FastAPI()
SERVICE_B_URL = "http://service_b:8001/items"

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    Получить информацию о товаре по ID.
    - **item_id**: ID товара
    """
    response = requests.get(f"{SERVICE_B_URL}/{item_id}")
    return response.json()

@app.post("/items/")
def create_item(item: dict):
    """
    Создать новый товар.
    - **item**: Данные товара (например, имя и цена)
    """
    response = requests.post(SERVICE_B_URL, json=item)
    return response.json()

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    """
    Обновить информацию о товаре.
    - **item_id**: ID товара
    - **item**: Обновленные данные товара
    """
    response = requests.put(f"{SERVICE_B_URL}/{item_id}", json=item)
    return response.json()

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Удалить товар по ID.
    - **item_id**: ID товара
    """
    response = requests.delete(f"{SERVICE_B_URL}/{item_id}")
    return response.json()
