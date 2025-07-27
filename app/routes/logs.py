from fastapi import APIRouter
from app.services.logging import get_latest_logs

router = APIRouter()

@router.get("/", summary="Get latest system logs")
def read_logs():
    logs = get_latest_logs(limit=100)
    return {"logs": logs}
