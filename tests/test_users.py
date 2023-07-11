import pytest
import requests
from unittest.mock import patch

def test_user_endpoint_unauthorized(mocker):
    url = "https://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    mocker.patch("requests.get")
    response_mock = mocker.MagicMock()
    response_mock.status_code = 401
    response_mock.json.return_value = None
    requests.get.return_value = response_mock

    response = requests.get(url, params=params, verify=False)

    assert response.status_code == 401
    assert not response.json()
    # Add more assertions based on your expected response

def test_user_endpoint_authorized(mocker):
    url = "https://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    mocker.patch("requests.get")
    response_mock = mocker.MagicMock()
    response_mock.status_code = 200
    response_mock.json.return_value = None
    requests.get.return_value = response_mock

    response = requests.get(url, params=params, verify=False)

    assert response.status_code == 200
    assert not response.json()
    # Add more assertions based on your expected response
