from datetime import date

import pytest

from nhl_data.models.schedule import ScheduleDate

schedule_test_cases = {
    "date_converted": (
        {"date": "2023-01-01"},
        ScheduleDate(date=date(2023, 1, 1)),
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
