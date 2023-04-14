import logging
from http import HTTPMethod

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

    def request(
        self, method: HTTPMethod, endpoint: str, url_parameters: dict = None
    ) -> httpx.Response:
        """
        Performs a HTTP Request to the specified endpoint.

        :param method: the specific request type we want to send
        :param endpoint: endpoint we want to send the request to
        :param url_parameters: any additional parameters to add for the request,
            defaults to None
        :return: the response object
        """
        response = self.client.request(method, endpoint, params=url_parameters)
        return self._handle_response(response)

    def _handle_response(self, response: httpx.Response) -> dict | list:
        if self.raise_status_errors:
            if response.status_code >= 500:
                raise HttpServerError(response.status_code)
            elif response.status_code >= 400:
                raise HttpClientError(response.status_code)
        return response

    def get(self, endpoint: str, url_parameters: dict = None) -> httpx.Response:
        """
        Performs a GET Request to the specified endpoint.

        :param method: the specific request type we want to send
        :param endpoint: endpoint we want to send the request to
        :param url_parameters: any additional parameters to add for the request,
            defaults to None
        :return: the JSON response from the request
        """
        return self.request(
            HTTPMethod.GET, endpoint=endpoint, url_parameters=url_parameters
        )


class HttpClientError(Exception):
    pass


class HttpServerError(Exception):
    pass
