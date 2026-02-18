def recursion(harvest):
    if harvest <= 0:
        return
    recursion(harvest - 1)
    print("Day: ", harvest)


def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))
    recursion(harvest)
    print("Harvest time!")
