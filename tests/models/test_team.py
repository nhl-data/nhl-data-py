import pytest

from nhl_data.models.team import Team, TeamLeader, TeamRecord, TeamRosterSpot

team_test_cases = {
    "short_team": (
        {"id": 1, "name": "The NHL Team"},
        Team(id=1, name="The NHL Team"),
    ),
    "empty_data": (dict(), Team()),
    "data_from_camel_case": ({"teamName": "Team Name"}, Team(team_name="Team Name")),
}


@pytest.mark.parametrize(
    ("test_data", "expected"), team_test_cases.values(), ids=team_test_cases.keys()
)
def test_team_from_response_json(test_data, expected):
    result = Team.from_response(test_data)
    assert result == expected


record_cases = {
    "only_points": (
        {"points": 100},
        TeamRecord(points=100),
    ),
    "empty_data": (dict(), TeamRecord()),
    "data_from_camel_case": ({"regulationWins": 50}, TeamRecord(regulation_wins=50)),
}


@pytest.mark.parametrize(
    ("test_data", "expected"), record_cases.values(), ids=record_cases.keys()
)
def test_team_record_from_response_json(test_data, expected):
    result = TeamRecord.from_response(test_data)
    assert result == expected


leader_cases = {
    "only_season": (
        {"season": "some_season"},
        TeamLeader(season="some_season"),
    ),
    "empty_data": (dict(), TeamLeader()),
    "data_from_camel_case": (
        {"leaderCategory": "some_category"},
        TeamLeader(leader_category="some_category"),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"), leader_cases.values(), ids=leader_cases.keys()
)
def test_team_leader_from_response_json(test_data, expected):
    result = TeamLeader.from_response(test_data)
    assert result == expected


roster_spot_cases = {
    "position_dict_keys_renamed": (
        {"position": {"positionKey": "C"}},
        TeamRosterSpot(position={"position_key": "C"}),
    ),
    "empty_data": (dict(), TeamRosterSpot()),
    "data_from_camel_case": (
        {"jerseyNumber": "99"},
        TeamRosterSpot(jersey_number="99"),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"), roster_spot_cases.values(), ids=roster_spot_cases.keys()
)
def test_team_roster_spot_from_respon_json(test_data, expected):
    result = TeamRosterSpot.from_response(test_data)
    assert result == expected
