# learning-FastAPI

FastAPI + SQLAlchemy + SQLite を使ったシンプルな Todo API の学習用プロジェクトです。

## このプロジェクトで学べること

- FastAPI を使った REST API の基本的な作り方（GET / POST / PUT / DELETE）
- Pydantic によるリクエストボディの型定義・バリデーション（`Field` での文字数制限など）
- SQLAlchemy ORM によるモデル定義（`models.py`）とテーブル作成
- `sessionmaker` / `Depends` を使った DB セッションの管理（リクエストごとに接続を作成・クローズ）
- SQLite をバックエンドにした簡単な永続化
- パスパラメータ・レスポンスモデルなしでの単純な CRUD API の構成

## ディレクトリ構成

```
.
├── main.py        # FastAPI アプリ本体（エンドポイント定義）
├── database.py    # DB接続・セッションの設定
├── models.py      # SQLAlchemyモデル（テーブル定義）
└── todos.db        # SQLiteデータベースファイル
```

## 起動方法

### 1. 必要なパッケージをインストール

```bash
pip install fastapi uvicorn sqlalchemy
```

### 2. サーバーを起動

```bash
uvicorn main:app --reload
```

### 3. 動作確認

ブラウザで以下にアクセスすると、Swagger UI から各エンドポイントを試せます。

```
http://127.0.0.1:8000/docs
```

## API エンドポイント一覧

| メソッド | パス | 説明 |
| --- | --- | --- |
| GET | `/` | 動作確認用のメッセージを返す |
| GET | `/todos` | Todo を全件取得 |
| GET | `/todos/{todo_id}` | 指定した ID の Todo を取得 |
| POST | `/todos` | Todo を新規作成 |
| PUT | `/todos/{todo_id}` | 指定した ID の Todo を更新 |
| DELETE | `/todos/{todo_id}` | 指定した ID の Todo を削除 |

### リクエストボディ例（POST / PUT）

```json
{
  "title": "牛乳を買う",
  "done": false
}
```
