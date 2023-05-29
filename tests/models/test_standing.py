import pytest

from nhl_data.models.standing import Standing
from nhl_data.models.team import Team, TeamRecord

standing_cases = {
    "standings_type": (
        {"standingsType": "someType"},
        Standing(standings_type="someType"),
    ),
    "league": (
        {"league": {"name": "NHL"}},
        Standing(league={"name": "NHL"}),
    ),
    "division": (
        {"division": {"name": "Pacific"}},
        Standing(division={"name": "Pacific"}),
    ),
    "conference": (
        {"conference": {"name": "West"}},
        Standing(conference={"name": "West"}),
    ),
    "team_record": (
        {"teamRecords": [{"team": {"id": 10}, "points": 100}]},
        Standing(team_records=[Team(id=10, record=TeamRecord(points=100))]),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    standing_cases.values(),
    ids=standing_cases.keys(),
)
def test_standing_from_response(test_data, expected):
    result = Standing.from_response(test_data)
    print(result)
    assert result == expected
