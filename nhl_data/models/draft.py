from __future__ import annotations

import datetime
from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.team import Team
from nhl_data.models.utils import convert_keys_to_snake_case


@dataclass
class Prospect(Model):
    """
    Represents and contains data for a given prospect from a draft,
    returned from the NHL API.
    """

    id: int = None
    full_name: str = None
    first_name: str = None
    last_name: str = None
    birth_date: str = None
    birth_city: str = None
    birth_state_province: str = None
    birth_country: str = None
    height: str = None
    weight: int = None
    shoots_catches: str = None
    primary_position: dict[str, str] = None
    nhl_player_id: int = None
    draft_status: str = None
    prospect_category: dict = None
    amateur_team: Team = None
    amateur_league: dict = None
    ranks: dict[str, int] = None

    @classmethod
    def from_response(cls, request_data: dict):
        data = convert_keys_to_snake_case(request_data)
        return cls(
            id=data.get("id"),
            full_name=data.get("full_name"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            birth_date=datetime.datetime.strptime(data["birth_date"], "%Y-%m-%d").date()
            if "birth_date" in data
            else None,
            birth_city=data.get("birth_city"),
            birth_state_province=data.get("birth_state_province"),
            birth_country=data.get("birth_country"),
            height=data.get("height"),
            weight=data.get("weight"),
            shoots_catches=data.get("shoots_catches"),
            primary_position=data.get("primary_position"),
            nhl_player_id=data.get("nhl_player_id"),
            draft_status=data.get("draft_status"),
            prospect_category=data.get("prospect_category"),
            amateur_team=Team.from_response(data["amateur_team"])
            if "amateur_team" in data
            else None,
            amateur_league=data.get("amateur_league"),
            ranks=data.get("ranks"),
        )
