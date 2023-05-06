from __future__ import annotations

from dataclasses import dataclass

from nhl_data.models.base import Model
from nhl_data.models.utils import convert_keys_to_snake_case


@dataclass
class Stat(Model):
    """
    Represents and contains all data for stat type, returned from the NHL API.
    """

    stat_type: str = None
    splits: list[dict] = None

    def from_response(cls, data: dict):
        data = convert_keys_to_snake_case(data)
        return cls(
            stat_type=data.get("type", dict()).get("displayName"),
            splits=data.get("splits"),
        )
