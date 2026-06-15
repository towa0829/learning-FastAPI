from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import engine, SessionLocal
import models

# データベーステーブルを作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# 型定義
class Todo(BaseModel):
  title: str = Field(..., min_length=1, max_length=100)
  done: bool = False

@app.get("/")
def read_root():
  return {"message": "Hello, World!"}

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
  return db.query(models.Todo).all()

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
  return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

@app.post("/todos", status_code=201)
def create_todo(todo: Todo, db: Session = Depends(get_db)):
  db_todo = models.Todo(title=todo.title, done=todo.done)
  db.add(db_todo)
  db.commit()
  db.refresh(db_todo)
  return db_todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo, db: Session = Depends(get_db)):
  db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

  if db_todo is None:
    raise HTTPException(status_code=404, detail="Todo not found")
  
  db_todo.title = todo.title
  db_todo.done = todo.done
  db.commit()
  db.refresh(db_todo)

  return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
  db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

  if db_todo is None:
    raise HTTPException(status_code=404, detail="Todo not found")
  
  db.delete(db_todo)
  db.commit()

  return {"message": "Todo deleted successfully"}