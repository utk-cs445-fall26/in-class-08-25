import argparse
from parser import load_events, count_by_event, filter_by_user


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user")
    args = ap.parse_args()

    events = load_events("data/events.csv")
    if args.user:
        events = filter_by_user(events, args.user)

    print("Event counts:")
    for event, count in sorted(count_by_event(events).items()):
        print(f"  {event}: {count}")


if __name__ == "__main__":
    main()
