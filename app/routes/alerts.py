from fastapi import APIRouter
from app.services.prediction import is_anomaly

router = APIRouter()

@router.get("/", summary="Check for anomalies")
def check_anomaly():
    """
    Endpoint untuk cek apakah ada anomali.
    """
    return {"anomaly_detected": is_anomaly()}
