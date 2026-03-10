from trace_utils import filter_by_date, filter_by_user

EVENTS = [
    {"date": "2026-03-01", "user": "u1", "event": "login", "target": ""},
    {"date": "2026-03-02", "user": "u2", "event": "logout", "target": ""},
]


def test_filter_by_date():
    assert filter_by_date(EVENTS, "2026-03-01") == [EVENTS[0]]


def test_filter_by_user():
    assert filter_by_user(EVENTS, "u2") == [EVENTS[1]]
