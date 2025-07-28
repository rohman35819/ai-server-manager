import sys
import os

# Tambahkan path root project ke sys.path agar "app" dikenali
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from app.routes import metrics, logs, alerts

app = FastAPI(title="AI Server Management API")

# Register all routers
app.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])

@app.get("/")
def root():
    return {"message": "AI Server Manager is running"}
