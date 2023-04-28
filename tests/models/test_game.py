import pytest

from nhl_data.models.game import Boxscore, Game, Play
from nhl_data.models.team import Team

game_test_cases = {
    "short_game": (
        {"gameData": {"game": {"pk": 2000020001}}},
        Game(pk=2000020001),
    ),
    "empty_data": (dict(), Game()),
    "team_within_game": (
        {"gameData": {"teams": {"away": {"id": 1}}}},
        Game(away_team=Team(id=1)),
    ),
    "play_within_game": (
        {"liveData": {"plays": {"allPlays": [{"result": {"event": "Start"}}]}}},
        Game(all_plays=[Play(event="Start")]),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"), game_test_cases.values(), ids=game_test_cases.keys()
)
def test_game_from_response(test_data, expected):
    result = Game.from_response(test_data)
    assert result == expected


play_test_cases = {
    "short_play": (
        {"result": {"description": "Game"}},
        Play(description="Game"),
    ),
    "empty_data": (dict(), Play()),
    "penalty_play": (
        {"result": {"penaltySeverity": "Minor", "penaltyMinutes": 2}},
        Play(penalty_severity="Minor", penalty_minutes=2),
    ),
    "scoring_play": (
        {"result": {"gameWinningGoal": False, "emptyNet": False}},
        Play(game_winning_goal=False, empty_net=False),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"), play_test_cases.values(), ids=play_test_cases.keys()
)
def test_play_from_response(test_data, expected):
    result = Play.from_response(test_data)
    assert result == expected


boxscore_test_cases = {
    "short_boxscore": (
        {"teams": {"away": {"goalies": [123456]}}},
        Boxscore(away_goalies=[123456]),
    ),
    "empty_data": (dict(), Boxscore()),
    "team_within_boxscore": (
        {"teams": {"away": {"team": {"id": 1, "name": "Team"}}}},
        Boxscore(away_team=Team(id=1, name="Team")),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    boxscore_test_cases.values(),
    ids=boxscore_test_cases.keys(),
)
def test_boxscore_from_response(test_data, expected):
    result = Boxscore.from_response(test_data)
    assert result == expected
