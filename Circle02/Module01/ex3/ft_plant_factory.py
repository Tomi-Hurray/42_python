class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    @staticmethod
    def show_header():
        print("=== Plant Factory Output ===")

    def show_info(self):
        print(f"Created: {self.name.capitalize()} ({self.height}cm, \
{self.age} days)")


def hf_total_created(plant):
    print("Total plants created:", plant)


if __name__ == "__main__":
    i = 0
    Plant.show_header()
my_plants = [
    Plant("Kaktus", 5.55, 26),
    Plant("Ser", 11.0, 2),
    Plant("róża", 11.5, 3),
    Plant("Lily", 6, 12),
    Plant("Oak", 200, 365)
]
for plant in my_plants:
    plant.show_info()
    i += 1
hf_total_created(i)
