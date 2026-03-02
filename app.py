from parser import load_events, count_by_event


def main():
    events = load_events("data/events.csv")
    print("Event counts:")
    for event, count in sorted(count_by_event(events).items()):
        print(f"  {event}: {count}")


if __name__ == "__main__":
    main()
