import requests
import pytest

def test_user_endpoint():
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(url, params=params)

    assert response.status_code == 200
    # Add more assertions based on your expected response

