import pytest

from nhl_data.models.season import Season

season_test_cases = {
    "short_data": (
        {"seasonId": "2000020001"},
        Season(season_id="2000020001"),
    ),
    "empty_data": (dict(), Season()),
}


@pytest.mark.parametrize(
    ("test_data", "expected"), season_test_cases.values(), ids=season_test_cases.keys()
)
def test_season_from_resposne(test_data, expected):
    result = Season.from_response(test_data)
    assert result == expected
