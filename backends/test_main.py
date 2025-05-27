"""
APIテスト
"""
from fastapi.testclient import TestClient

from backends.main import app

client = TestClient(app)

def test_hello():
    """ Hello World """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello World"
        }

def test_info():
    """ Infomation """
    response = client.get("/api/info")
    assert response.status_code == 200

def test_xor_gate():
    """ XOR回路 """
    a = 1.0
    b = 1.0
    response = client.get(
        "/api/xor_gate",
        params={"a":a, "b":b}
        )
    assert response.status_code == 200
    assert response.json() == {
        "result": 0
        }
