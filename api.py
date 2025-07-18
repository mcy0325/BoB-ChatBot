from fastapi import FastAPI
import logging
 
app = FastAPI()

@app.get("/")
async def root():
    logging.info("Hello World")
    return {"message": "Hello World"}

@app.get("/profile")
async def profile():
    return {
        "name": "문채영",
        "major": "소프트웨어학과",
        "generation": "BoB 14기",
        "message": "보안제품개발 트랙 교육생입니다!"
    }