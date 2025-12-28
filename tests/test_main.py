import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_nyito_oldal_mukodik():
    response = client.get("/")
    assert response.status_code == 200
    assert "uzenet" in response.json()

@pytest.mark.parametrize("vegpont, elvart_kod", [
    ("/statisztika/", 200),
    ("/adatok/", 200),
    ("/nem_letezo_oldal/", 404)
])
def test_vegpontok_elerhetosege(vegpont, elvart_kod):
    response = client.get(vegpont)
    assert response.status_code == elvart_kod

def test_adatlista_limit():
    response = client.get("/adatok/?limit=1")
    adatok = response.json()
    assert isinstance(adatok, list)
    
    assert len(adatok) <= 1