"""
Module containing all relevant functionality related to the Stats NHL API.
"""

from http import HTTPMethod

from nhl_data.api.http_client import HttpClient
from nhl_data.models import Game, ScheduleDate, Season, Team


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
        """
        Pulls data from the `teams` endpoint. This method expands some of the endpoints
        that are normally not included. This includes:

        - leaders
        - records
        - roster

        If `team_ids` is not specified, it will pull data from every single team.
        If `season_start_year` is not specified, it will pull data from the
        current season.

        :param team_ids: the specific teams we want to pull,
            defaults to pulling every team
        :param season_start_year: the season we want to pull from,
            defaults to pulling from the current season
        :return: team data represented in custom models
        """
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

    def game(self, game_id: int) -> Game:
        """
        Pulls data from the `game` endpoint. This method specific retrieves the live
        feed data for a specific game.

        :param game_id: the specific game we want to look at
        :return: all game data for a specific game
        """
        url = f"/game/{game_id}/feed/live"
        game_data = self.get(url)
        return Game.from_response(game_data)

    def seasons(self) -> list[Season]:
        """
        Pulls data from the `seasons` endpoint.

        :return: summary data for every season in the NHL, represented as a list
            of Season models
        """
        url = "/seasons"
        seasons_data = self.get(url).get("seasons", [])
        return [Season.from_response(data) for data in seasons_data]

    def schedule(
        self,
        team_ids: list[int] = None,
        season: int = None,
        start_date: str = None,
        end_date: str = None,
    ) -> list[ScheduleDate]:
        """
        Pulls data from the `schedule` endpoint. This method fetches data containing
        general information about various games / events from different dates.

        If `team_ids` is specified, then the method will filter to all dates containing
        the specified teams. If nothing is specified, then it searches for all teams.

        If `season` is specified, then the method will search for dates in the specified
        season. If nothing is specified, then it searches for the current season.

        If `start_date` AND `end_date` is specified, then the method will find
        all the games in the specified date range. If one or both are missing,
        it searches for current day's games.

        :param team_ids: specific teams we want search for, defaults to None
        :param season: specific season we want to search on, defaults to None
        :param start_date: the beginning of a date range we want to search on,
            defaults to None
        :param end_date: the end of a date range we want to search on, default to None
        :return: list of ScheduleDate models which contains summary data for each date
            retrieved
        """
        url = "/schedule"
        params = {
            "teamId": ",".join(str(x) for x in team_ids) if team_ids else None,
            "startDate": start_date,
            "endDate": end_date,
            "season": f"{season}{season+1}" if season else None,
        }
        data = self.get(url, url_parameters=params).get("dates", [])
        return [ScheduleDate.from_response(d) for d in data]
