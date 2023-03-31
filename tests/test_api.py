from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_above_50k(above_50):
    r = client.post("/predict", json=above_50)
    assert r.json() == {'prediction': '>50K'}


def test_below_50k(below_50):
    r = client.post("/predict", json=below_50)
    assert r.json() == {'prediction': '<=50K'}
