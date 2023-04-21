import pytest

from nhl_data.models.team import Team

test_cases = {
    "short_team": (
        {"id": 1, "name": "The NHL Team"},
        Team(id=1, name="The NHL Team"),
    ),
    "empty_data": (dict(), Team()),
    "data_from_camel_case": ({"teamName": "Team Name"}, Team(team_name="Team Name")),
}


@pytest.mark.parametrize(
    ("test_data", "expected"), test_cases.values(), ids=test_cases.keys()
)
def test_team_from_response_json(test_data, expected):
    result = Team.from_response(test_data)
    assert result == expected
