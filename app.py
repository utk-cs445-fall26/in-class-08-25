import argparse
from trace_utils import load_events, count_by_event, filter_by_user, filter_by_date


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user")
    ap.add_argument("--date", help="YYYY-MM-DD")
    args = ap.parse_args()

    events = load_events("data/events.csv")
    if args.user:
        events = filter_by_user(events, args.user)
    if args.date:
        events = filter_by_date(events, args.date)

    print("Event counts:")
    for event, count in sorted(count_by_event(events).items()):
        print(f"  {event}: {count}")


if __name__ == "__main__":
    main()
