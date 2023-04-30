from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.utils import convert_keys_to_snake_case


@dataclass
class Season(Model):
    """
    Represents a summary for the season.
    Contains data on how many games were played, and how standings were used that year.
    """

    season_id: str = None
    regular_season_start_date: str = None
    regular_season_end_date: str = None
    season_end_date: str = None
    number_of_games: int = None
    ties_in_use: bool = None
    olympics_participation: bool = None
    conferences_in_use: bool = None
    divisions_in_use: bool = None
    wild_card_in_use: bool = None

    @classmethod
    def from_response(cls, response_data: dict):
        data = convert_keys_to_snake_case(response_data)
        return cls(
            season_id=data.get("season_id"),
            regular_season_start_date=data.get("regular_season_start_date"),
            regular_season_end_date=data.get("regular_season_end_date"),
            season_end_date=data.get("season_end_date"),
            number_of_games=data.get("number_of_games"),
            ties_in_use=data.get("ties_in_use"),
            olympics_participation=data.get("olympics_participation"),
            conferences_in_use=data.get("conferences_in_use"),
            divisions_in_use=data.get("divisions_in_use"),
            wild_card_in_use=data.get("wild_card_in_use"),
        )
