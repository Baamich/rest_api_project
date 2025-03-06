from fastapi import FastAPI, HTTPException

app = FastAPI()
items_db = {}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in items_db:
        return {"item_id": item_id, "data": items_db[item_id]}
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/")
def create_item(item: dict):
    item_id = len(items_db) + 1
    items_db[item_id] = item
    return {"item_id": item_id, "data": item}
