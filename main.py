from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SE-final FastAPI 啟動成功！"}
    