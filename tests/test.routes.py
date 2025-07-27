client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_metrics():
    response = client.get("/metrics/")
    assert response.status_code == 200
