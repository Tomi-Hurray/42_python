class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.__name = name
        self.__height = 0.0
        self.__age = 0

        self.set_age(age)
        self.set_height(height)
    # SET VALUES

    def set_height(self, height: float):
        if (self.checker(self.__age, height)):
            self.__height = height

    def set_age(self, age: int):
        if (self.checker(age, self.__height)):
            self.__age = age

    def set_name(self, name: str):
        self.__name = name
    # GET VALUES

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name
    # CHECKER

    def checker(self, age: int, height: float):
        if (age < 0):
            print("Error, age cannot be negative")
            return 0
        if (height < 0.0):
            print("Error, height cannot be negative")
            return 0
        return 1


def show_header():
    print("== Garden Plant Types ==\n")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.__color_attribute = color

    def bloom(self):
        if (self.get_age() >= 30):
            print(f"{self.__color_attribute.capitalize()} {self.get_name()} \
is blooming beautifully!\n".title())
        else:
            print(f"{self.__color_attribute.capitalize()} {self.get_name()} \
is too young to bloom...\n")

    def get_info(self):
        print(f"{self.get_name()} (Flower): {self.get_height()}cm,\
 {self.get_age()} days, {self.__color_attribute} color")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: int):
        super().__init__(name, height, age)
        self.__trunk_diamater = trunk_diameter

    def produce_shade(self):
        shade: float = self.__trunk_diamater * 1.2
        print(f"{self.get_name().capitalize()} provides {shade} \
square meters of shade!\n")

    def get_info(self):
        print(f"{self.get_name()} (Tree): {self.get_height()}cm,\
 {self.get_age()} days, {self.__trunk_diamater}cm diamater")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: bool):
        super().__init__(name, height, age)
        self.__harvest_season = harvest_season
        self.__nutritional_value = nutritional_value

    def healthy(self):
        if (self.__nutritional_value == 1):
            print(f"{self.get_name()} is healthy for you!\n")
        else:
            print("Don't eat that!\n")

    def get_info(self):
        print(f"{self.get_name()} (Vegetable): {self.get_height()}cm,\
 {self.get_age()} days, {self.__harvest_season} harvest")

# MAIN FUNCTION


if __name__ == "__main__":
    show_header()
    my_flowers = [
        Flower("Rose", 25, 30, "Red"),
        Flower("Lily", 10.2, 28, "White")
    ]
    my_trees = [
        Tree("Oak", 350, 1825, 50),
        Tree("Birch", 250, 900, 35)
    ]
    my_vegetables = [
        Vegetable("Tomato", 80, 90, "summer", True),
        Vegetable("Wheat", 150, 90, "autumn", False)
    ]

    for flower in my_flowers:
        flower.get_info()
        flower.bloom()
    for tree in my_trees:
        tree.get_info()
        tree.produce_shade()
    for veg in my_vegetables:
        veg.get_info()
        veg.healthy()
