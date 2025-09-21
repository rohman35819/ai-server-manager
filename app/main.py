from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="AI Server Manager")

app.include_router(chat_router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "AI Server Manager is running"}
