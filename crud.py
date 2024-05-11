from fastapi import FastAPI
from pydantic import BaseModel
from database import Database
import uvicorn

app = FastAPI()

# Create a class that inherits from BaseModel
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Create an instance of the Database class
db = Database("store.db")

# insert 10 sample items into the database
for i in range(1, 11):
    db.insert(f"Item {i}", f"Description of item {i}", 9.99, 0.99)

# Create a route to get all items
@app.get("/items/")
async def get_items():
    # Get all items from the database
    items = db.view()
    return {"items": items}

@app.post("/items/")
async def create_item(item: Item):
    # Insert the item into the database
    db.insert(item.name, item.description, item.price, item.tax)
    return {"message": "Item created successfully"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    # Get the item with the specified ID from the database
    item = db.search(id=item_id)
    return {"item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # Update the item with the specified ID in the database
    db.update(item_id, item.name, item.description, item.price, item.tax)
    return {"message": "Item updated successfully"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    # Delete the item with the specified ID from the database
    db.delete(item_id)
    return {"message": "Item deleted successfully"}

# Run the FastAPI application
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)