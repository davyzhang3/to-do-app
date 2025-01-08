from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TodoItem(BaseModel):
    text: str

# A simple in-memory store for todos
todos: List[str] = ["Buy milk"]

@app.get("/todos")
def get_todos():
    """Retrieve all todos."""
    return {"todos": todos}

@app.post("/todos")
def add_todo(item: TodoItem):
    """Add a todo to the list."""
    todos.append(item.text)
    return {"message": "Todo added successfully", "todo": item.text}