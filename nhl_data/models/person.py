from __future__ import annotations

import datetime
from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.team import Team
from nhl_data.models.utils import convert_keys_to_snake_case


@dataclass
class Person(Model):
    """
    Represents and contains all data for a person, returned from the NHL API.
    """

    id: int = None
    full_name: str = None
    first_name: str = None
    last_name: str = None
    primary_number: str = None
    birth_date: datetime.date = None
    current_age: int = None
    birth_city: str = None
    birth_state_province: str = None
    birth_country: str = None
    nationality: str = None
    height: str = None
    weight: int = None
    active: bool = None
    alternate_captain: bool = None
    captain: bool = None
    rookie: bool = None
    shoots_catches: str = None
    roster_status: str = None
    current_team: Team = None
    primary_position: dict = None
    social: dict = None
    stats: list = None

    @classmethod
    def from_response(cls, response_data: dict) -> Person:
        data = convert_keys_to_snake_case(response_data)
        return cls(
            id=data.get("id"),
            full_name=data.get("full_name"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            primary_number=data.get("primary_number"),
            birth_date=datetime.datetime.strptime(data["birth_date"], "%Y-%m-%d").date()
            if "birth_date" in data
            else None,
            current_age=data.get("current_age"),
            birth_city=data.get("birth_city"),
            birth_state_province=data.get("birth_state_province"),
            birth_country=data.get("birth_country"),
            nationality=data.get("nationality"),
            height=data.get("height"),
            weight=data.get("weight"),
            active=data.get("active"),
            alternate_captain=data.get("alternate_captain"),
            captain=data.get("captain"),
            rookie=data.get("rookie"),
            shoots_catches=data.get("shoots_catches"),
            roster_status=data.get("roster_status"),
            current_team=Team.from_response(data["current_team"])
            if "current_team" in data
            else None,
            primary_position=data.get("primary_position"),
            social=data.get("social"),
            stats=data.get("stats"),
        )
