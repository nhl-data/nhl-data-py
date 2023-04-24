from __future__ import annotations

import logging
from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.utils import convert_keys_to_snake_case

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Team(Model):
    """
    Represents and contains all data for a single team, returned from the NHL API.
    """

    id: int = None
    name: str = None
    link: str = None
    venue: dict = None
    abbreviation: str = None
    team_name: str = None
    location_name: str = None
    first_year_of_play: int = None
    division: dict = None
    conference: dict = None
    franchise: dict = None
    team_stats: list = None
    team_leaders: list[TeamLeader] = None
    short_name: str = None
    record: TeamRecord = None
    official_site_url: str = None
    active: bool = None

    @classmethod
    def from_response(cls, data: dict) -> Team:
        data = convert_keys_to_snake_case(data)
        record_data = (
            TeamRecord.from_response(data.get("record")) if "record" in data else None
        )
        team_leaders = (
            [TeamLeader.from_response(d) for d in data.get("team_leaders")]
            if "team_leaders" in data
            else None
        )
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            link=data.get("link"),
            venue=data.get("venue"),
            abbreviation=data.get("abbreviation"),
            team_name=data.get("team_name"),
            location_name=data.get("location_name"),
            first_year_of_play=data.get("first_year_of_play"),
            division=data.get("division"),
            conference=data.get("conference"),
            franchise=data.get("franchise"),
            team_stats=data.get("teamStats"),
            team_leaders=team_leaders,
            short_name=data.get("shortName"),
            record=record_data,
            official_site_url=data.get("official_site_url"),
            active=data.get("active"),
        )


@dataclass(frozen=True)
class TeamRecord(Model):
    """Represents all records / stats for a given team."""

    league_record: dict = None
    regulation_wins: int = None
    goals_against: int = None
    goals_scored: int = None
    points: int = None
    division_rank: str = None
    division_l10_rank: str = None
    division_road_rank: str = None
    division_home_rank: str = None
    conference_rank: str = None
    conference_l10_rank: str = None
    conference_road_rank: str = None
    conference_home_rank: str = None
    league_rank: str = None
    leage_l10_rank: str = None
    league_road_rank: str = None
    league_home_rank: str = None
    wild_card_rank: str = None
    row: int = None
    games_played: int = None
    streak: dict = None
    clinch_indicator: str = None
    points_percentage: float = None
    pp_division_rank: str = None
    pp_conference_rank: str = None
    pp_league_rank: str = None
    last_updated: str = None

    @classmethod
    def from_response(cls, json_response: dict) -> TeamRecord:
        data = convert_keys_to_snake_case(json_response)
        return cls(
            league_record=data.get("league_record"),
            regulation_wins=data.get("regulation_wins"),
            goals_against=data.get("goals_against"),
            goals_scored=data.get("goals_scored"),
            points=data.get("points"),
            division_rank=data.get("division_rank"),
            division_l10_rank=data.get("division_l10_rank"),
            division_road_rank=data.get("division_road_rank"),
            division_home_rank=data.get("division_home_rank"),
            conference_rank=data.get("conference_rank"),
            conference_l10_rank=data.get("conference_l10_rank"),
            conference_road_rank=data.get("conference_road_rank"),
            conference_home_rank=data.get("conference_home_rank"),
            league_rank=data.get("league_rank"),
            leage_l10_rank=data.get("leage_l10_rank"),
            league_road_rank=data.get("league_road_rank"),
            league_home_rank=data.get("league_home_rank"),
            wild_card_rank=data.get("wild_card_rank"),
            row=data.get("row"),
            games_played=data.get("games_played"),
            streak=data.get("streak"),
            clinch_indicator=data.get("clinch_indicator"),
            points_percentage=data.get("points_percentage"),
            pp_division_rank=data.get("pp_division_rank"),
            pp_conference_rank=data.get("pp_conference_rank"),
            pp_league_rank=data.get("pp_league_rank"),
            last_updated=data.get("last_updated"),
        )


@dataclass(frozen=True)
class TeamLeader(Model):
    """Represents the Leaders for a specific stat."""

    leader_category: str = None
    depth: str = None
    player_status: str = None
    season: str = None
    game_type: dict = None
    limits: dict = None
    limit_metadata: dict = None
    leaders: list[dict] = None

    @classmethod
    def from_response(cls, json_response: dict) -> TeamLeader:
        data = convert_keys_to_snake_case(json_response)
        return cls(
            leader_category=data.get("leader_category"),
            depth=data.get("depth"),
            player_status=data.get("player_status"),
            season=data.get("season"),
            game_type=data.get("game_type"),
            limits=data.get("limits"),
            limit_metadata=data.get("limit_metadata"),
            leaders=data.get("leaders"),
        )
