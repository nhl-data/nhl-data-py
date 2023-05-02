import datetime
from dataclasses import dataclass

from nhl_data.models.base import Model
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
            total_events=data.get("total_items"),
            total_games=data.get("total_items"),
            total_matches=data.get("total_items"),
            games=data.get("games"),
            events=data.get("events"),
            matches=data.get("matches"),
        )
