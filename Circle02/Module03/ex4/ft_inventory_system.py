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
    print(f"Got inventory: {inventory}")
    return (inventory)


def inventory_system_list(inventory: dict) -> list:
    inventory_list = list(inventory)
    print(f"Inventory list: {inventory_list}")
    return inventory_list


def inventory_system_calc_sum(inventory: dict) -> int:
    sum_of_items = 0
    for i in inventory.values():
        sum_of_items += i
    return sum_of_items


def inventory_system_calc_num(inventory: dict) -> int:
    num_of_items = 0
    for j in inventory.keys():
        num_of_items += 1
    return num_of_items


def inventory_system_calc_misc(inventory: dict, inventory_list: list,
                               sum_of_items: int) -> None:
    for x, y in zip(inventory.values(), inventory_list):
        percent = round(((x / sum_of_items) * 100), 1)
        print(f"Item {y} represents {percent}%")


def inventory_system_calc_abundance(inventory: dict) -> None:
    most_ab_name = None
    most_ab_value = 0
    least_ab = float("inf")
    least_ab_name = None
    for item, value in inventory.items():
        if value > most_ab_value:
            most_ab_name = item
            most_ab_value = value
        if least_ab > value:
            least_ab_name = item
            least_ab = value
    if (least_ab == float("inf")):
        least_ab = 0
    print(f"Item most abundant: {most_ab_name} with "
          f"quantity {most_ab_value}")
    print(f"Item least abundant: {least_ab_name} with "
          f"quantity {least_ab}")


def inventory_system_update(inventory: dict[str, int]) -> dict:
    inventory['magic item'] = 1
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    input = sys.argv
    inventory = parser(input)
    inventory_list = inventory_system_list(inventory)
    sum_of_items = inventory_system_calc_sum(inventory)
    num_of_items = inventory_system_calc_num(inventory)
    print(f"Total quantity of the {num_of_items} items: {sum_of_items}")
    inventory_system_calc_misc(inventory, inventory_list, sum_of_items)
    inventory_system_calc_abundance(inventory)
    print(f"Updated inventory: {inventory_system_update(inventory)}")
