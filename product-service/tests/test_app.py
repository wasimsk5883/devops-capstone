
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Product Service is running!"
    }


def test_products_endpoint(client):
    response = client.get("/products")
    assert response.status_code == 200

    products = response.get_json()
    assert len(products) == 3
    assert products[0]["name"] == "Laptop"
    assert products[0]["price"] == 55000


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
