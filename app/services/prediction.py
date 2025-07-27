import joblib
from app.services.monitoring import get_server_metrics
import os

MODEL_PATH = "app/models/anomaly_model.pkl"

def is_anomaly():
    if not os.path.exists(MODEL_PATH):
        return False  # assume safe if no model

    model = joblib.load(MODEL_PATH)
    metrics = get_server_metrics()
    X = [[metrics["cpu"], metrics["memory"], metrics["disk"]]]
    result = model.predict(X)
    return result[0] == -1
