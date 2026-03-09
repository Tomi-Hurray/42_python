
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    @staticmethod
    def show_header():
        print("=== Garden Plant Registry ===")

    def show_info(self):
        print(f"{self.name.capitalize()} : {self.height}cm, \
{self.age} days old")


if __name__ == "__main__":
    Plant.show_header()
my_plants = [
    Plant("Kaktus", 5.55, 26),
    Plant("Ser", 11.0, 2),
    Plant("róża", 11.5, 3)
]
for plant in my_plants:
    plant.show_info()
