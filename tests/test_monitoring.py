from app.services.monitoring import get_server_metrics

def test_metrics_keys():
    metrics = get_server_metrics()
    assert "cpu" in metrics
    assert "memory" in metrics
    assert "disk" in metrics
