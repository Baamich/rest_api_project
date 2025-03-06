from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()
items_db = {}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Получить информацию о товаре по ID.
    - **item_id**: ID товара
    """
    if item_id in items_db:
        return {"item_id": item_id, "data": items_db[item_id]}
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/")
def create_item(item: dict):
    """
    Создать новый товар.
    - **item**: Данные товара
    """
    item_id = len(items_db) + 1
    items_db[item_id] = item
    return {"item_id": item_id, "data": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    """
    Обновить информацию о товаре.
    - **item_id**: ID товара
    - **item**: Обновленные данные товара
    """
    if item_id in items_db:
        items_db[item_id] = item
        return {"item_id": item_id, "data": item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Удалить товар по ID.
    - **item_id**: ID товара
    """
    if item_id in items_db:
        del items_db[item_id]
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
