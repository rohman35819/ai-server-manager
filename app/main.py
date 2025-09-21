from fastapi import FastAPI
from app.routes.metrics import router as metrics_router
from app.routes.logs import router as logs_router
from app.routes.alerts import router as alerts_router
from app.routes.command import router as command_router

app = FastAPI(title="AI Server Management API")

# Register routers
app.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])
app.include_router(logs_router, prefix="/logs", tags=["Logs"])
app.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])
app.include_router(command_router, prefix="/command", tags=["Command"])
@app.get("/")
def root():
    return {"message": "AI Server Manager is running"}
