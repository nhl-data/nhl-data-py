import datetime

import pytest

from nhl_data.models.schedule import ScheduleDate, ScheduleGame
from nhl_data.models.team import Team

schedule_test_cases = {
    "date_converted": (
        {"date": "2023-01-01"},
        ScheduleDate(date=datetime.date(2023, 1, 1)),
    ),
    "total_items": ({"totalItems": 0}, ScheduleDate(total_items=0)),
    "total_events": ({"totalEvents": 0}, ScheduleDate(total_events=0)),
    "total_games": ({"totalGames": 0}, ScheduleDate(total_games=0)),
    "total_matches": ({"totalMatches": 0}, ScheduleDate(total_matches=0)),
    "games": (
        {"games": [{"gamePk": 1}, {"gamePk": 2}]},
        ScheduleDate(games=[ScheduleGame(game_pk=1), ScheduleGame(game_pk=2)]),
    ),
    "empty_data": (dict(), ScheduleDate()),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    schedule_test_cases.values(),
    ids=schedule_test_cases.keys(),
)
def test_schedule_date_from_resposne(test_data, expected):
    result = ScheduleDate.from_response(test_data)
    assert result == expected


schedule_game_test_cases = {
    "game_pk": ({"gamePk": 1}, ScheduleGame(game_pk=1)),
    "game_type": ({"gameType": "P"}, ScheduleGame(game_type="P")),
    "season": ({"season": "20202021"}, ScheduleGame(season="20202021")),
    "game_date": (
        {"game_date": "2023-01-01T01:30:00Z"},
        ScheduleGame(
            game_date=datetime.datetime(
                2023, 1, 1, 1, 30, 0, tzinfo=datetime.timezone.utc
            )
        ),
    ),
    "status": ({"status": dict()}, ScheduleGame(status=dict())),
    "away_data": (
        {"teams": {"away": {"leagueRecord": dict(), "score": 0, "team": {"id": 1}}}},
        ScheduleGame(away_league_record=dict(), away_score=0, away_team=Team(id=1)),
    ),
    "home_data": (
        {"teams": {"home": {"leagueRecord": dict(), "score": 0, "team": {"id": 1}}}},
        ScheduleGame(home_league_record=dict(), home_score=0, home_team=Team(id=1)),
    ),
    "venue": ({"venue": dict()}, ScheduleGame(venue=dict())),
    "empty_data": (dict(), ScheduleGame()),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    schedule_game_test_cases.values(),
    ids=schedule_game_test_cases.keys(),
)
def test_schedule_game_from_resposne(test_data, expected):
    result = ScheduleGame.from_response(test_data)
    assert result == expected
