from datetime import date

import pytest

from nhl_data.models.draft import DraftPick, DraftRound, Prospect
from nhl_data.models.team import Team

draft_round_test_cases = {
    "round_number": (
        {"roundNumber": 1},
        DraftRound(round_number=1),
    ),
    "round": (
        {"round": "1"},
        DraftRound(round="1"),
    ),
    "picks": (
        {"picks": [{"pickInRound": 1}, {"pickInRound": 2}]},
        DraftRound(picks=[DraftPick(pick_in_round=1), DraftPick(pick_in_round=2)]),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    draft_round_test_cases.values(),
    ids=draft_round_test_cases.keys(),
)
def test_draft_round_from_response(test_data, expected):
    result = DraftRound.from_response(test_data)
    assert result == expected


draft_pick_test_cases = {
    "year": (
        {"year": 2000},
        DraftPick(year=2000),
    ),
    "round": (
        {"round": "1"},
        DraftPick(round="1"),
    ),
    "pick_overall": (
        {"pickOverall": 1},
        DraftPick(pick_overall=1),
    ),
    "pick_in_round": (
        {"pickInRound": 1},
        DraftPick(pick_in_round=1),
    ),
    "team": (
        {"team": {"id": 10}},
        DraftPick(team=Team(id=10)),
    ),
    "prospect": (
        {"prospect": {"id": 10}},
        DraftPick(prospect=Prospect(id=10)),
    ),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    draft_pick_test_cases.values(),
    ids=draft_pick_test_cases.keys(),
)
def test_draft_pick_from_response(test_data, expected):
    result = DraftPick.from_response(test_data)
    assert result == expected


prospect_test_cases = {
    "id": (
        {"id": 111},
        Prospect(id=111),
    ),
    "full_name": (
        {"fullName": "Wayne Gretzky"},
        Prospect(full_name="Wayne Gretzky"),
    ),
    "first_name": (
        {"firstName": "Wayne"},
        Prospect(first_name="Wayne"),
    ),
    "last_name": (
        {"lastName": "Gretzky"},
        Prospect(last_name="Gretzky"),
    ),
    "birth_date": ({"birthDate": "2000-01-01"}, Prospect(birth_date=date(2000, 1, 1))),
    "birth_city": ({"birthCity": "Wonderland"}, Prospect(birth_city="Wonderland")),
    "birth_state_province": (
        {"birthStateProvince": "A"},
        Prospect(birth_state_province="A"),
    ),
    "height": ({"height": "7' 0\""}, Prospect(height="7' 0\"")),
    "weight": ({"weight": 200}, Prospect(weight=200)),
    "shoots_catches": ({"shootsCatches": False}, Prospect(shoots_catches=False)),
    "primary_position": (
        {"primaryPosition": {"code": "D"}},
        Prospect(primary_position={"code": "D"}),
    ),
    "nhl_player_id": ({"nhlPlayerId": 10000}, Prospect(nhl_player_id=10000)),
    "draft_status": ({"draftStatus": "Elig"}, Prospect(draft_status="Elig")),
    "prospect_category": (
        {"prospectCategory": {"id": 1}},
        Prospect(prospect_category={"id": 1}),
    ),
    "amateur_team": (
        {"amateurTeam": {"name": "Something"}},
        Prospect(amateur_team=Team(name="Something")),
    ),
    "amateur_league": (
        {"amateurLeague": {"name": "Some League"}},
        Prospect(amateur_league={"name": "Some League"}),
    ),
    "ranks": ({"ranks": {"finalRank": 1}}, Prospect(ranks={"final_rank": 1})),
}


@pytest.mark.parametrize(
    ("test_data", "expected"),
    prospect_test_cases.values(),
    ids=prospect_test_cases.keys(),
)
def test_prospect_from_response(test_data, expected):
    result = Prospect.from_response(test_data)
    assert result == expected
