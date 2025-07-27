from fastapi import APIRouter
from app.services.monitoring import get_server_metrics

router = APIRouter()

@router.get("/", summary="Get current server metrics")
def read_metrics():
    metrics = get_server_metrics()
    return {"status": "ok", "data": metrics}
