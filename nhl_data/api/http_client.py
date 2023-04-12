import logging

import httpx

logger = logging.getLogger(__name__)


class HttpClient:
    """
    HTTP Client for connecting to the NHL API.
    """

    def __init__(self, base_url: str, raise_status_errors: bool = True) -> None:
        self.base_url = base_url
        self.raise_status_errors = raise_status_errors
        self.client = httpx.Client(base_url=self.base_url, timeout=10)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.client.close()
