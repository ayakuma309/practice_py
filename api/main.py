from fastapi import FastAPI

# FastAPIのインスタンス
app = FastAPI()

# @ で始まるこの部分を、デコレータ と呼ぶ。
# デコレータは、以下の２つの部分に分かれる。
# - パス "/hello"
# - オペレーション  "get" の部分
@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
