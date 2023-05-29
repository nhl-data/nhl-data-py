from __future__ import annotations

from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.team import Team, TeamRecord
from nhl_data.models.utils import convert_keys_to_snake_case


@dataclass(frozen=True)
class Standing(Model):
    """Represents the standings of teams."""

    standings_type: str = None
    league: dict = None
    division: dict = None
    conference: dict = None
    team_records: list[Team] = None

    @classmethod
    def from_response(cls, json_response: dict) -> Standing:
        data = convert_keys_to_snake_case(json_response)
        records_data = data.get("team_records", [])
        print(records_data)
        teams = [
            Team(
                id=t.get("team", dict()).get("id"),
                name=t.get("team", dict()).get("name"),
                link=t.get("team", dict()).get("link"),
                record=TeamRecord.from_response(t),
            )
            for t in records_data
        ]
        return cls(
            standings_type=data.get("standings_type"),
            league=data.get("league"),
            division=data.get("division"),
            conference=data.get("conference"),
            team_records=teams if teams else None,
        )
