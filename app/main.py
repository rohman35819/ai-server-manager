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
