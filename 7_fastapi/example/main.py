from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

items_db = {}
current_id = 0

@app.post("/items")
def create_item(item: Item):
    global current_id
    current_id += 1
    items_db[current_id] = item
    return {"id": current_id, **item.dict()}

@app.get("/items")
def list_items():
    return [{"id": item_id, **item.dict()} for item_id, item in items_db.items()]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items_db:
        return {"id": item_id, **items_db[item_id].dict()}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, new_item: Item):
    if item_id in items_db:
        items_db[item_id] = new_item
        return {"id": item_id, **new_item.dict()}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items_db:
        del items_db[item_id]
        return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")