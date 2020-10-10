from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_rate_endpoint():
    response = client.get(
        '/rate/?base_currency=BGN&target_currency=AUD&exchange_date=2020-10-10')
    assert response.status_code == 200
    assert response.json() == {
        "id": response.json()['id'],
        "exchangeDate": "2020-10-10",
        "rate": 0.83879,
        "baseCurrency": "BGN",
        "targetCurrency": "AUD"
    }
