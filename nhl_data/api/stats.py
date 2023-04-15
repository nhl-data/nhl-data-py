"""
Module containing all relevant functionality related to the Stats NHL API.
"""

from http import HTTPMethod

from nhl_data.api.http_client import HttpClient


class StatsNhlApi:
    """Wrapper for the Stats NHL API."""

    base_url = "https://statsapi.web.nhl.com/api"

    def __init__(self, api_version=1) -> None:
        self.url = f"{self.base_url}/v{api_version}"
        self.version = api_version

    def request(
        self, method: HTTPMethod, endpoint: str, url_parameters: dict = None
    ) -> dict | list:
        """
        Sends an arbitrary request to the Stats NHL API.

        :param method: the specific HTTP Method to send
        :param endpoint: the endpoint we want to send the request to
        :param url_parameters: ny additional parameters to add for the request,
            defaults to None
        :return: the JSON response from the request
        """
        with HttpClient(self.base_url) as client:
            response = client.request(method, endpoint, url_parameters)
        return response.json()

    def get(self, endpoint: str, url_parameters: dict = None) -> dict | list:
        """
        Sends a GET request to the Stats NHL API.

        :param endpoint: the endpoint we want to send the request to
        :param url_parameters: ny additional parameters to add for the request,
            defaults to None
        :return: the JSON response from the request
        """
        with HttpClient(self.base_url) as client:
            response = client.get(endpoint, url_parameters)
        return response.json()
