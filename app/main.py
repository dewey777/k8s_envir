import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    message = os.environ.get("APP_MESSAGE", "🔧 기본 메시지입니다.")
    return {"message": message}
