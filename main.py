from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

# 型定義
class Todo(BaseModel):
  title: str
  done: bool = False

@app.get("/")
def read_root():
  return {"message": "Hello, World!"}

@app.get("/todos")
def get_todos():
  return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
  return todos[todo_id]

@app.post("/todos")
def create_todo(todo: Todo):
  todos.append(todo)
  return todo