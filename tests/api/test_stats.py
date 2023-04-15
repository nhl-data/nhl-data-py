from unittest.mock import patch

import httpx

from nhl_data import StatsNhlApi


@patch("nhl_data.api.http_client.HttpClient.request")
def test_request(mock_request):
    mock_request.return_value = httpx.Response(
        status_code=200, json={"random_key": "random_value"}
    )
    api = StatsNhlApi()
    response = api.request("GET", "/")
    assert response == {"random_key": "random_value"}


@patch("nhl_data.api.http_client.HttpClient.get")
def test_get(mock_request):
    mock_request.return_value = httpx.Response(
        status_code=200, json={"random_key": "random_value"}
    )
    api = StatsNhlApi()
    response = api.get("/")
    assert response == {"random_key": "random_value"}
