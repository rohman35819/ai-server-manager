from fastapi import APIRouter
from app.services.prediction import is_anomaly

router = APIRouter()

@router.get("/", summary="Check for anomalies")
def check_anomaly():
    return {"anomaly_detected": is_anomaly()}
