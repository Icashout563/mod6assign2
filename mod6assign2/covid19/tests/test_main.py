from fastapi.testclient import TestClient
from covid19.main import app

client = TestClient(app)

def test_covid_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "COVID API is running"}
