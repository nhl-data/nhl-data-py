from datetime import date

import pytest

from nhl_data.models.person import Person
from nhl_data.models.team import Team

person_cases = {
    "id": ({"id": 111111}, Person(id=111111)),
    "full_name": ({"fullName": "Wayne Gretzky"}, Person(full_name="Wayne Gretzky")),
    "first_name": ({"firstName": "Wayne"}, Person(first_name="Wayne")),
    "last_name": ({"lastName": "Gretzky"}, Person(last_name="Gretzky")),
    "primary_number": ({"primaryNumber": "99"}, Person(primary_number="99")),
    "birth_date": ({"birthDate": "2000-01-01"}, Person(birth_date=date(2000, 1, 1))),
    "current_age": ({"currentAge": 99}, Person(current_age=99)),
    "birth_city": ({"birthCity": "Wonderland"}, Person(birth_city="Wonderland")),
    "birth_state_province": (
        {"birthStateProvince": "A"},
        Person(birth_state_province="A"),
    ),
    "birth_country": ({"birthCountry": "USA"}, Person(birth_country="USA")),
    "nationality": ({"nationality": "USA"}, Person(nationality="USA")),
    "height": ({"height": "7' 0\""}, Person(height="7' 0\"")),
    "weight": ({"weight": 200}, Person(weight=200)),
    "active": ({"active": False}, Person(active=False)),
    "alternate_captain": ({"alternateCaptain": False}, Person(alternate_captain=False)),
    "captain": ({"captain": False}, Person(captain=False)),
    "rookie": ({"rookie": False}, Person(rookie=False)),
    "shoots_catches": ({"shoots_catches": False}, Person(shoots_catches=False)),
    "roster_status": ({"rosterStatus": False}, Person(roster_status=False)),
    "current_team": ({"currentTeam": {"id": 1}}, Person(current_team=Team(id=1))),
    "primary_position": (
        {"primaryPosition": {"code": "D"}},
        Person(primary_position={"code": "D"}),
    ),
    "empty_data": (dict(), Person()),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    person_cases.values(),
    ids=person_cases.keys(),
)
def test_schedule_date_from_resposne(test_data, expected):
    result = Person.from_response(test_data)
    assert result == expected
