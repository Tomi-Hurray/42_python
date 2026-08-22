import math


def get_player_pos():
    raw1 = []
    while len(raw1) != 3:
        raw1 = input("coords")
    print(f"First set of coordinates: {raw1}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    get_player_pos()
