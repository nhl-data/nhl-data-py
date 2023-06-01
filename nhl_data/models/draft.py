from __future__ import annotations

import datetime
from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.team import Team
from nhl_data.models.utils import convert_keys_to_snake_case


@dataclass
class Draft(Model):
    """Represents and contains all data for a given draft, returned from the NHL API."""

    draft_year: int = None
    rounds: list[DraftRound] = None

    @classmethod
    def from_response(cls, request_data: dict):
        data = convert_keys_to_snake_case(request_data)
        return cls(
            draft_year=data.get("draft_year"),
            rounds=[DraftRound.from_response(d) for d in data["rounds"]]
            if "rounds" in data
            else None,
        )


@dataclass
class DraftRound(Model):
    """
    Represents and contains all data for a given round in a draft,
    returned from the NHL API.
    """

    round_number: int = None
    round: str = None
    picks: list[DraftPick] = None

    @classmethod
    def from_response(cls, request_data: dict):
        data = convert_keys_to_snake_case(request_data)
        return cls(
            round_number=data.get("round_number"),
            round=data.get("round"),
            picks=[DraftPick.from_response(d) for d in data["picks"]]
            if "picks" in data
            else None,
        )


@dataclass
class DraftPick(Model):
    """
    Represents and contains all data for a given pick in a draft,
    returned from the NHL API.
    """

    year: int = None
    round: str = None
    pick_overall: int = None
    pick_in_round: int = None
    team: Team = None
    prospect: Prospect = None

    @classmethod
    def from_response(cls, request_data: dict):
        data = convert_keys_to_snake_case(request_data)
        return cls(
            year=data.get("year"),
            round=data.get("round"),
            pick_overall=data.get("pick_overall"),
            pick_in_round=data.get("pick_in_round"),
            team=Team.from_response(data["team"]) if "team" in data else None,
            prospect=Prospect.from_response(data["prospect"])
            if "prospect" in data
            else None,
        )


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
