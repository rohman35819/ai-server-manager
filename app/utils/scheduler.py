import time
from app.services.monitoring import get_server_metrics
from app.services.prediction import is_anomaly

def run_monitor(interval=60):
    while True:
        metrics = get_server_metrics()
        if is_anomaly():
            print("🚨 Anomaly Detected!", metrics)
        else:
            print("✅ All good:", metrics)
        time.sleep(interval)
