import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_root():
    app = FastAPI()
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


def test_hello(name="World"):
    app = FastAPI()
    client = TestClient(app)
    response = client.get("/hello/{}".format(name))
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, {}".format(name)}


if __name__ == "__main__":
    pytest.main()