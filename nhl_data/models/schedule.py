import datetime
from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.team import Team
from nhl_data.models.utils import convert_keys_to_snake_case


@dataclass
class ScheduleDate(Model):
    """
    Represents a summary for the season.
    Contains data on how many games were played, and how standings were used that year.
    """

    date: datetime.date = None
    total_items: int = None
    total_events: int = None
    total_games: int = None
    total_matches: int = None
    games: list = None
    events: list = None
    matches: list = None

    @classmethod
    def from_response(cls, response_data: dict):
        data = convert_keys_to_snake_case(response_data)
        return cls(
            date=datetime.datetime.strptime(data["date"], "%Y-%m-%d").date()
            if "date" in data
            else None,
            total_items=data.get("total_items"),
            total_events=data.get("total_events"),
            total_games=data.get("total_games"),
            total_matches=data.get("total_matches"),
            games=[ScheduleGame.from_response(d) for d in data["games"]]
            if "games" in data
            else None,
            events=data.get("events"),
            matches=data.get("matches"),
        )


@dataclass
class ScheduleGame(Model):
    """
    Represents a Game from the Schedule object.
    This is different from the `Game` object since it contains less data
    but also contains fields that do not exist in the other models.
    """

    game_pk: int = None
    game_type: str = None
    season: str = None
    game_date: datetime.datetime = None
    status: dict = None
    away_league_record: dict = None
    away_score: int = None
    away_team: Team = None
    home_league_record: dict = None
    home_score: int = None
    home_team: Team = None
    venue: dict = None

    @classmethod
    def from_response(cls, response_data: dict):
        data = convert_keys_to_snake_case(response_data)
        away = data.get("teams", dict()).get("away", dict())
        home = data.get("teams", dict()).get("home", dict())
        return cls(
            game_pk=data.get("game_pk"),
            game_type=data.get("game_type"),
            season=data.get("season"),
            game_date=datetime.datetime.fromisoformat(data.get("game_date"))
            if "game_date" in data
            else None,
            status=data.get("status"),
            away_league_record=away.get("league_record"),
            away_score=away.get("score"),
            away_team=Team.from_response(away["team"]) if "team" in away else None,
            home_league_record=home.get("league_record"),
            home_score=home.get("score"),
            home_team=Team.from_response(home["team"]) if "team" in home else None,
            venue=data.get("venue"),
        )
