# learning-FastAPI

FastAPI + SQLAlchemy + SQLite を使ったシンプルな Todo API の学習用プロジェクトです。JWT を使ったユーザー認証も実装しています。

## このプロジェクトで学べること

- FastAPI を使った REST API の基本的な作り方（GET / POST / PUT / DELETE）
- Pydantic によるリクエストボディの型定義・バリデーション（`Field` での文字数制限など）
- SQLAlchemy ORM によるモデル定義（`models.py`）とテーブル作成
- `sessionmaker` / `Depends` を使った DB セッションの管理（リクエストごとに接続を作成・クローズ）
- SQLite をバックエンドにした簡単な永続化
- パスパラメータ・レスポンスモデルなしでの単純な CRUD API の構成
- `passlib` によるパスワードのハッシュ化（bcrypt）
- `python-jose` による JWT アクセストークンの発行・検証
- `OAuth2PasswordBearer` / `OAuth2PasswordRequestForm` を使ったログイン認証フローの実装

## ディレクトリ構成

```
.
├── main.py        # FastAPI アプリ本体（エンドポイント定義）
├── database.py    # DB接続・セッションの設定
├── models.py      # SQLAlchemyモデル（テーブル定義）
├── auth.py        # パスワードハッシュ化・JWT検証などの認証ロジック
└── todos.db        # SQLiteデータベースファイル
```

## 起動方法

### 1. 必要なパッケージをインストール

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose python-multipart
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
| POST | `/register` | ユーザーを新規登録 |
| POST | `/login` | ログインしてアクセストークンを取得 |
| GET | `/me` | ログイン中のユーザー情報を取得（認証必須） |
| GET | `/todos` | Todo を全件取得 |
| GET | `/todos/{todo_id}` | 指定した ID の Todo を取得 |
| POST | `/todos` | Todo を新規作成 |
| PUT | `/todos/{todo_id}` | 指定した ID の Todo を更新 |
| DELETE | `/todos/{todo_id}` | 指定した ID の Todo を削除 |

### リクエストボディ例（POST / PUT `/todos`）

```json
{
  "title": "牛乳を買う",
  "done": false
}
```

### 認証フロー

1. `POST /register` にユーザー名・パスワードを送って新規登録する

```json
{
  "username": "alice",
  "password": "password123"
}
```

2. `POST /login` に `username` / `password` を `form-data` で送るとアクセストークンが返る

```json
{
  "access_token": "xxxxx.yyyyy.zzzzz",
  "token_type": "bearer"
}
```

3. 取得したトークンを `Authorization: Bearer <access_token>` ヘッダーに付けてリクエストすると、`GET /me` などの認証が必要なエンドポイントにアクセスできる
