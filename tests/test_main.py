from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_nyito_oldal_mukodik():
    response = client.get("/")
    assert response.status_code == 200
    assert "uzenet" in response.json()

def test_statisztika_mukodik():
    response = client.get("/statisztika/")
    assert response.status_code == 200
    adatok = response.json()
    assert "atlag_ar_huf" in adatok

def test_adatlista_nem_ures():
    response = client.get("/adatok/?limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)