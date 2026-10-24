import os
import sys
import pytest

# Add cart-service directory to Python's import path
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

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
        "message": "Cart Service is running!"
    }


def test_cart_endpoint(client):
    response = client.get("/cart")
    assert response.status_code == 200

    cart = response.get_json()
    assert len(cart) == 2
    assert cart[0]["name"] == "Laptop"
    assert cart[0]["quantity"] == 1
    assert cart[1]["name"] == "Keyboard"
    assert cart[1]["quantity"] == 2


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
