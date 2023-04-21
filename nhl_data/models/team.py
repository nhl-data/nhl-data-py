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
    short_name: str = None
    official_site_url: str = None
    active: bool = None

    @classmethod
    def from_response(cls, data: dict) -> Team:
        data = convert_keys_to_snake_case(data)
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
            short_name=data.get("shortName"),
            official_site_url=data.get("official_site_url"),
            active=data.get("active"),
        )
