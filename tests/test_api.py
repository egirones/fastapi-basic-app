from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_above_50k(above_50):
    """
    Test tha prediction is above 50k
    """
    r = client.post("/predict", json=above_50)
    assert r.status_code == 200
    assert r.json() == {'prediction': '>50K'}


def test_below_50k(below_50):
    """
    Test tha prediction is below 50k
    """
    r = client.post("/predict", json=below_50)
    assert r.status_code == 200
    assert r.json() == {'prediction': '<=50K'}


def test_api_get_root():
    """
    Test api get root
    """
    r = client.get("/")
    assert r.json() == {"message": "Hello World"}
    assert r.status_code == 200
