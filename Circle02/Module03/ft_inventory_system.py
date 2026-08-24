import sys


def parser(input: list) -> dict:
    inventory = {}
    sum_of_items = 0
    for i in input[1:]:
        if ":" not in i:
            print(f"Invalid parameter - '{i}'")
            continue
        name, quantity = i.split(":")
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(quantity)
            sum_of_items += int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    print(inventory)
    return (inventory)


def inventory_system_list(inventory: dict) -> list:
    inventory_list = list(inventory)
    print(f"{inventory_list}")
    return inventory_list


def inventory_system_calc(inventory: dict) -> int:
    sum_of_items = 0
    num_of_items = 0
    for i in inventory.values():
        sum_of_items += i
    num_of_items = len(inventory.keys)
    return sum_of_items


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    input = sys.argv
    inventory = parser(input)
    inventory_system_list(inventory)
    sum_of_items = inventory_system_calc(inventory)
