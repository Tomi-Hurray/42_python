
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def to_grow(self):
        self.height += 1
        self.age += 1
        self.growth += 1

    def show_info(self):
        print(f"{self.name.capitalize()} : {self.height}cm, \
{self.age} days old")

    def summary(self):
        print(f"Growth this week of {self.name}: {self.growth}cm")


def get_total_info(my_plants: list):
    for day in range(0, 7):
        print(f"=== DAY {day + 1} ==")
        for plant in my_plants:
            if day > 0:
                plant.to_grow()

            plant.show_info()
    for plant in my_plants:
        plant.summary()


if __name__ == "__main__":

    my_plants = [
        Plant("Kaktus", 5.55, 26),
        Plant("Ser", 11.0, 2),
        Plant("róża", 11.5, 3)
    ]

get_total_info(my_plants)
