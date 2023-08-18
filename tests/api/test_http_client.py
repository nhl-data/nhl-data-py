import asyncio
from unittest.mock import AsyncMock, Mock

import httpx
import pytest

from nhl_data.api.http_client import (
    HttpClient,
    HttpClientAsync,
    HttpClientError,
    HttpServerError,
)

TEST_URL = "https://testing.com"


def test_request():
    expected = {"random_key": "random_value"}
    mock_client = Mock()
    mock_client.request.return_value = httpx.Response(
        status_code=200, json={"random_key": "random_value"}
    )
    with HttpClient(TEST_URL) as c:
        c.client = mock_client
        result = c.request("GET", "/")
    assert result.status_code == 200
    assert result.json() == expected


@pytest.mark.asyncio
async def test_async_request():
    expected = {"random_key": "random_value"}
    mock_client = AsyncMock()
    mock_client.request.return_value = httpx.Response(
        status_code=200, json={"random_key": "random_value"}
    )
    async with HttpClientAsync(TEST_URL) as c:
        c.client = mock_client
        result = await c.request("GET", "/")
    assert result.status_code == 200
    assert result.json() == expected


@pytest.mark.asyncio
async def test_async_request_timed():
    """Ensure that all requests are not being made synchronously."""

    async def mock_request(*args, **kwargs):
        await asyncio.sleep(0.2)
        return httpx.Response(status_code=200, json={"random_key": "random_value"})

    expected = {"random_key": "random_value"}
    mock_client = AsyncMock()
    mock_client.request.side_effect = mock_request
    async with HttpClientAsync(TEST_URL) as c:
        c.client = mock_client
        start_time = asyncio.get_event_loop().time()
        results = await asyncio.gather(*[c.request("GET", "/") for _ in range(10)])
        end_time = asyncio.get_event_loop().time()
    assert end_time - start_time < 2
    assert all(r.status_code == 200 for r in results)
    assert all(r.json() == expected for r in results)


def test_get():
    expected = {"random": "value"}
    mock_client = Mock()
    mock_client.request.return_value = httpx.Response(
        status_code=200, json={"random": "value"}
    )
    with HttpClient(TEST_URL) as c:
        c.client = mock_client
        result = c.get("/")
    assert result.status_code == 200
    assert result.json() == expected


@pytest.mark.asyncio
async def test_async_get():
    expected = {"random_key": "random_value"}
    mock_client = AsyncMock()
    mock_client.request.return_value = httpx.Response(
        status_code=200, json={"random_key": "random_value"}
    )
    async with HttpClientAsync(TEST_URL) as c:
        c.client = mock_client
        result = await c.get("/")
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
