from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
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
  title: str
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

@app.post("/todos")
def create_todo(todo: Todo, db: Session = Depends(get_db)):
  db_todo = models.Todo(title=todo.title, done=todo.done)
  db.add(db_todo)
  db.commit()
  db.refresh(db_todo)
  return db_todo