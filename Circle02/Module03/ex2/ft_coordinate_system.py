import math


def get_player_pos() -> tuple:
    while True:
        temp = []
        raw1 = input("Enter new coordinates as floats in format 'x,y,z': ")
        list1 = raw1.split(',')
        try:
            for i in list1:
                temp.append(float(i))
            coords1 = tuple(temp)
        except ValueError:
            print("Invalid syntax.")
            continue
        if len(coords1) != 3:
            print("Not eneough elements!")
            continue
        return (coords1)


def calculate_distance_to_center(coords: tuple) -> float:
    x, y, z = coords
    distance_center = math.sqrt(math.pow((x - 0), 2) + math.pow((y - 0), 2)
                                + math.pow((z - 0), 2))

    return distance_center


def calculate_distance_between(coords1: tuple, coords2: tuple) -> float:
    x1, y1, z1 = coords1
    x2, y2, z2 = coords2
    distance_b = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)
                           + math.pow((z1 - z2), 2))
    return distance_b


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coords1 = get_player_pos()
    print(f"Got a first tuple: {coords1}")
    distance_c = calculate_distance_to_center(coords1)
    print(f"It includes: X={coords1[0]}, Y={coords1[1]}, Z={coords1[2]}")
    print(f"Distance to center: {distance_c}")
    print("Get a second set of coordinates")
    coords2 = get_player_pos()
    distance_b = calculate_distance_between(coords1, coords2)
    print(f"Distance between the 2 sets of coordinates: {distance_b}")
