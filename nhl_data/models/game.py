from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.utils import convert_keys_to_snake_case


@dataclass
class Game(Model):
    """
    Represents and contains all data for a given game, returned from the NHL API.
    """

    pk: int = None
    season: str = None
    type: str = None
    date_time: str = None
    end_date_time: str = None
    abstract_game_state: str = None
    coded_game_state: str = None
    detailed_state: str = None
    status_code: str = None
    away: dict = None
    home: dict = None
    players: dict = None
    venue: dict = None
    all_plays: list = None
    scoring_plays: list = None
    penalty_plays: list = None
    plays_by_period: list = None
    current_play: dict = None
    boxscore: dict = None
    decisions: dict = None

    @classmethod
    def from_request(cls, request_data: dict):
        data = convert_keys_to_snake_case(request_data)
        game_data, live_data = data.get("game_data", dict()), data.get(
            "live_data", dict()
        )
        return cls(
            pk=game_data.get("game", dict()).get("pk"),
            season=game_data.get("game", dict()).get("season"),
            type=game_data.get("game", dict()).get("game_type"),
            date_time=game_data.get("date_time", dict()).get("date_time"),
            end_date_time=game_data.get("date_time", dict()).get("end_date_time"),
            abstract_game_state=game_data.get("status", dict()).get(
                "abstract_game_state"
            ),
            coded_game_state=game_data.get("status", dict()).get("coded_game_state"),
            detailed_state=game_data.get("status", dict()).get("detailed_state"),
            status_code=game_data.get("status", dict()).get("status_code"),
            players=game_data.get("players"),
            venue=game_data.get("venue"),
            all_plays=live_data.get("plays", dict()).get("all_plays"),
            scoring_plays=live_data.get("plays", dict()).get("scoring_plays"),
            penalty_plays=live_data.get("plays", dict()).get("penalty_plays"),
            plays_by_period=live_data.get("plays", dict()).get("plays_by_period"),
            current_play=live_data.get("plays", dict()).get("current_play"),
            boxscore=live_data.get("boxscore"),
            decisions=live_data.get("decisions"),
        )
