import csv


def load_events(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def count_by_event(events):
    counts = {}
    for event in events:
        key = event["event"]
        counts[key] = counts.get(key, 0) + 1
    return counts


def filter_by_user(events, user):
    return [event for event in events if event["user"] == user]


def filter_by_date(events, target_date):
    return [event for event in events if event["date"] == target_date]


def count_failed_logins(events):
    return sum(1 for event in events if event["event"] == "login_failed")
