from unittest.mock import Mock

import httpx
import pytest

from nhl_data.api.http_client import HttpClient, HttpClientError, HttpServerError

TEST_URL = "https://testing.com"


def test_request():
    expected = {"random_key": "random_value"}
    mock_response = Mock()
    mock_response.request.return_value = httpx.Response(
        status_code=200, json={"random_key": "random_value"}
    )
    with HttpClient(TEST_URL) as c:
        c.client = mock_response
        result = c.request("GET", "/")
    assert result.status_code == 200
    assert result.json() == expected


def test_get():
    expected = {"random": "value"}
    mock_response = Mock()
    mock_response.request.return_value = httpx.Response(
        status_code=200, json={"random": "value"}
    )
    with HttpClient(TEST_URL) as c:
        c.client = mock_response
        result = c.get("/")
    assert result.status_code == 200
    assert result.json() == expected


@pytest.mark.parametrize(("status"), [400, 500])
def test_status_error_raise_exception(status):
    error = HttpServerError if status >= 500 else HttpClientError
    data = {"should": "error"}
    response = Mock(status_code=status, json=data)
    with pytest.raises(error, match=f"{status}"):
        HttpClient(TEST_URL)._handle_response(response)


@pytest.mark.parametrize(("status"), [400, 500])
def test_status_error_dont_raise_exception(status):
    data = {"show_up": "even_on_error"}
    response = httpx.Response(status_code=status, json=data)
    with HttpClient(TEST_URL, raise_status_errors=False) as c:
        val = c._handle_response(response)
    assert val.json() == data
