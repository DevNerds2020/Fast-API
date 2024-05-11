from database import Database
from models import Todo
from fastapi import FastAPI

app = FastAPI()

db = Database("todo.db")

@app.get("/todos/")
async def get_todos():
    todos = db.view()
    return {"todos": todos}

@app.post("/todos/")
async def create_todo(todo: Todo):
    db.insert(todo.task, todo.status)
    return {"message": "Todo created successfully"}

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    todo = db.search(id=todo_id)
    return {"todo": todo}

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    db.update(todo_id, todo.task, todo.status)
    return {"message": "Todo updated successfully"}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    db.delete(todo_id)
    return {"message": "Todo deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)