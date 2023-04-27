from __future__ import annotations

from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.team import Team
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
    away_team: Team = None
    home_team: Team = None
    players: dict = None
    venue: dict = None
    all_plays: list[Play] = None
    scoring_plays: list = None
    penalty_plays: list = None
    plays_by_period: list = None
    current_play: Play = None
    boxscore: dict = None
    decisions: dict = None

    @classmethod
    def from_response(cls, request_data: dict):
        data = convert_keys_to_snake_case(request_data)
        game_data = data.get("game_data", dict())
        live_data = data.get("live_data", dict())
        plays_data = live_data.get("plays", dict())
        all_plays = (
            [Play.from_response(d) for d in plays_data.get("all_plays", [])]
            if "all_plays" in plays_data
            else None
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
            away_team=Team.from_response(game_data.get("teams", dict()).get("away"))
            if "away" in game_data.get("teams", dict())
            else None,
            home_team=Team.from_response(game_data.get("teams", dict()).get("home"))
            if "home" in game_data.get("teams", dict())
            else None,
            players=game_data.get("players"),
            venue=game_data.get("venue"),
            all_plays=all_plays,
            scoring_plays=plays_data.get("scoring_plays"),
            penalty_plays=plays_data.get("penalty_plays"),
            plays_by_period=plays_data.get("plays_by_period"),
            current_play=Play.from_response(plays_data["current_play"])
            if "current_play" in plays_data
            else None,
            boxscore=live_data.get("boxscore"),
            decisions=live_data.get("decisions"),
        )


@dataclass
class Play(Model):
    """
    Represents and contains all data for a single play from an NHL game.
    """

    players: list = None
    event: str = None
    event_type_id: str = None
    description: str = None
    secondary_type: str = None
    strength_name: str = None
    game_winning_goal: bool = None
    empty_net: bool = None
    penalty_severity: str = None
    penalty_minutes: str = None
    period: int = None
    period_type: str = None
    ordinal_num: str = None
    period_time: str = None
    period_time_remaining: str = None
    date_time: str = None
    goals_away: int = None
    goals_home: int = None
    coordinates: dict = None
    team: Team = None

    @classmethod
    def from_response(cls, request_data: dict):
        data = convert_keys_to_snake_case(request_data)
        result_data = data.get("result", dict())
        about_data = data.get("about", dict())
        return cls(
            players=data.get("players"),
            event=result_data.get("event"),
            event_type_id=result_data.get("event_type_id"),
            description=result_data.get("description"),
            secondary_type=result_data.get("secondary_type"),
            strength_name=result_data.get("strength", dict()).get("name"),
            game_winning_goal=result_data.get("game_winning_goal"),
            empty_net=result_data.get("empty_net"),
            penalty_severity=result_data.get("penalty_severity"),
            penalty_minutes=result_data.get("penalty_minutes"),
            period=about_data.get("period"),
            period_type=about_data.get("period_type"),
            ordinal_num=about_data.get("ordinal_num"),
            period_time=about_data.get("period_time"),
            period_time_remaining=about_data.get("period_time_remaining"),
            date_time=about_data.get("date_time"),
            goals_away=about_data.get("goals", dict()).get("away"),
            goals_home=about_data.get("goals", dict()).get("home"),
            coordinates=data.get("coordinates"),
            team=Team.from_response(data["team"]) if "team" in data else None,
        )
