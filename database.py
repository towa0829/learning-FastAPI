from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# データベースファイルへの接続経路を作る
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  connect_args = {"check_same_thread": False}
)
# セッションを作るための型
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデル（テーブル定義）の土台となるクラス
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
