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
