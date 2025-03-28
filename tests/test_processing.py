import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import make_operations1


@pytest.mark.parametrize(
    'state, expected',
    [
        ("EXECUTED", [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]),
        ("CANCELED", [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ])
    ]
)
def test_filter_by_state_with_make_operations1(make_operations1, state, expected) -> None:
    assert filter_by_state(make_operations1, state) == expected


@pytest.mark.parametrize(
    'state, expected',
    [
        ("EXECUTED", "Операции с данным статусом отсутствуют"),
        ("CANCELED", [
            {"id": 41428829, "state": "CANCELED", "date": "2019-07-32T18:35:29.512364"},
            {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ])
    ]
)
def test_filter_by_state_with_make_operations2(make_operations2, state, expected) -> None:
    assert filter_by_state(make_operations2, state) == expected


@pytest.mark.parametrize(
    'state, expected',
    [
        ("EXECUTED", "Статус одной или нескольких операций не указан!"),
        ("CANCELED", "Статус одной или нескольких операций не указан!")
    ]
)
def test_filter_by_state_with_make_operations3(make_operations3, state, expected) -> None:
    assert filter_by_state(make_operations3, state) == expected


@pytest.mark.parametrize(
    'state, expected',
    [
        ("EXECUTED", ("Статус одной или нескольких операций не указан!")),
        ("CANCELED", ("Статус одной или нескольких операций не указан!"))
    ]
)
def test_filter_by_state_with_make_operations4(make_operations4, state, expected) -> None:
    assert filter_by_state(make_operations4, state) == expected


@pytest.mark.parametrize(
    'state, expected',
    [
        ("EXECUTED", ("Отсутствуют данные для обработки! Проверьте правильность ввода!")),
        ("CANCELED", ("Отсутствуют данные для обработки! Проверьте правильность ввода!"))
    ]
)
def test_filter_by_state_with_make_operations5(make_operations5, state, expected) -> None:
    assert filter_by_state(make_operations5, state) == expected


@pytest.mark.parametrize(
    'flow, expected', [
    (True, [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    (False, [
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ])]

)
def test_sort_by_date_with_make_operations1(make_operations1, flow, expected) -> None:
    assert sort_by_date(make_operations1, flow) == expected


@pytest.mark.parametrize(
    'flow, expected', [
    (True, "Дата и время одной или нескольких операций имеют неверный формат!"),
    (False, "Дата и время одной или нескольких операций имеют неверный формат!")]
)
def test_sort_by_date_with_make_operations2(make_operations2, flow, expected) -> None:
    assert sort_by_date(make_operations2, flow) == expected


@pytest.mark.parametrize(
    'flow, expected', [
    (True, [
            {'id': 41428829, 'date': '2019-07-03'},
            {'id': 615064591, 'date': '2018-10-14'},
            {'id': 594226727, 'date': '2018-09-12'},
            {'id': 939719570, 'date': '2018-06-30'}
    ]),
    (False, [
            {'id': 939719570, 'date': '2018-06-30'},
            {'id': 594226727, 'date': '2018-09-12'},
            {'id': 615064591, 'date': '2018-10-14'},
            {'id': 41428829, 'date': '2019-07-03'}
    ])]

)
def test_sort_by_date_with_make_operations3(make_operations3, flow, expected) -> None:
    assert sort_by_date(make_operations3, flow) == expected

@pytest.mark.parametrize(
    'flow, expected', [
    (True, "Дата и время одной или нескольких операций не указаны!"),
    (False, "Дата и время одной или нескольких операций не указаны!")]
)
def test_sort_by_date_with_make_operations4(make_operations4, flow, expected) -> None:
    assert sort_by_date(make_operations4, flow) == expected


@pytest.mark.parametrize(
    'flow, expected', [
    (True, "Отсутствуют данные для обработки! Проверьте правильность ввода!"),
    (False, "Отсутствуют данные для обработки! Проверьте правильность ввода!")]
)
def test_sort_by_date_with_make_operations5(make_operations5, flow, expected) -> None:
    assert sort_by_date(make_operations5, flow) == expected