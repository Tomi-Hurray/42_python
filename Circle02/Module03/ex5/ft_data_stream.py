import random


def gen_event(players: list, actions: list):
    while True:
        player = players[random.randint(0, 3)]
        action = actions[random.randint(0, 6)]
        yield player, action


def consume_event(events: list):
    while events:
        print(f"Remains in list: {events}")
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        print(f"Got event from list: {event}")
        yield event
    print(f"Remains in list: {events}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    players = ["Alice", "Bob", "Dylan", "Charlie"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
    new_event = ()
    gen = gen_event(players, actions)
    events = [10]
    for num in range(1, 11):
        new_event = next(gen)
        print(f"Event {num}: {new_event[0]} did action {new_event[1]}")

    events = [next(gen) for _ in range(10)]
    for c in consume_event(events):
        pass
