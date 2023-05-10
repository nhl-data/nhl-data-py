import pytest

from nhl_data.models.stat import Stat

stat_cases = {
    "stat_type": (
        {"type": {"displayName": "some_stat_type"}},
        Stat(stat_type="some_stat_type"),
    ),
    "splits": (
        {"splits": [{"split1": 1}, {"split2": 2}]},
        Stat(splits=[{"split1": 1}, {"split2": 2}]),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    stat_cases.values(),
    ids=stat_cases.keys(),
)
def test_stat_from_resposne(test_data, expected):
    result = Stat.from_response(test_data)
    assert result == expected
