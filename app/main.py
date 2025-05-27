import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    message = os.getenv("APP_MESSAGE", "🔧 기본 메시지입니다.")
    secret = os.getenv("APP_SECRET", "❌ 비밀 없음")
    return {
        "message": message,
        "secret": secret
    }
