from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_create_transaction_success():
    payload = {
        "manager": "Ivan",
        "amount": 500.0
    }
    response = client.post("/transactions", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["manager"] == "Ivan"
    assert data["amount"] == 500.0
    assert isinstance("id" in data)