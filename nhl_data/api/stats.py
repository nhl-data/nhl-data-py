"""
Module containing all relevant functionality related to the Stats NHL API.
"""

from http import HTTPMethod

from nhl_data.api.http_client import HttpClient
from nhl_data.models.team import Team


class StatsNhlApi:
    """Wrapper for the Stats NHL API."""

    base_domain = "https://statsapi.web.nhl.com"

    def __init__(self, api_version=1) -> None:
        self.base_url = f"{self.base_domain}/api/v{api_version}"
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

    def teams(self, team_ids: list = [], season_start_year: int = None) -> list[Team]:
        expands = ["team.record", "team.leaders", "team.roster"]
        season = (
            f"{season_start_year}{season_start_year+1}" if season_start_year else None
        )
        with HttpClient(self.base_url) as client:
            leader_categories = [
                stat.get("displayName")
                for stat in client.get("/leagueLeaderTypes").json()
            ]
            params = {
                "teamId": ",".join([str(x) for x in team_ids]),
                "expand": ",".join(expands),
                "leaderCategories": ",".join(leader_categories),
                "season": season,
            }
            if season is None:
                del params["season"]
            response = client.get("/teams", url_parameters=params).json()
        return [Team.from_response(t) for t in response.get("teams")]
