from app.services.prediction import is_anomaly

def test_anomaly_check():
    result = is_anomaly()
    assert isinstance(result, bool)
