import pytest
from fastapi.testclient import TestClient
from main import app 

# Инициализация клиента для тестирования
@pytest.fixture
def client():
    return TestClient(app)

# Тест главной страницы
def test_mainpage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.content

# Тест для вычисления выражения
def test_calculate_expression(client):
    response = client.post("/calculate", json={"expression": "2 + 2"})
    assert response.status_code == 200
    assert response.json() == {"result": "4"} 

# Тест для вычисления cos
def test_cos(client):
    response = client.post("/cos", json={"expression": "0"})
    assert response.status_code == 200
    assert response.json() == {"result": "1.0"}  

# Тест для вычисления sin
def test_sin(client):
    response = client.post("/sin", json={"expression": "0"})
    assert response.status_code == 200
    assert response.json() == {"result": "0.0"}  

# Тест для вычисления tan
def test_tan(client):
    response = client.post("/tan", json={"expression": "0"})
    assert response.status_code == 200
    assert response.json() == {"result": "0.0"}  

# Тест на обработку ошибок
def test_calculate_expression_error(client):
    response = client.post("/calculate", json={"expression": "invalid"})
    assert response.status_code == 400
    assert response.json() == {"result": "Error"}
