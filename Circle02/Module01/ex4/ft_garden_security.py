class SecurePlant:
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

    def get_hight(self):
        print(f"Height: {self.__height}")
        return self.__height

    def get_age(self):
        print(f"Age: {self.__age}")
        return self.__age
    # CHECKER

    def checker(self, age: int, height: float):
        if (age < 0):
            print("Error, age cannot be negative")
            return 0
        if (height < 0.0):
            print("Error, height cannot be negative")
            return 0
        return 1
    # INFO

    def show_info(self):
        print(f"Name: {self.__name}")
        print(f"Height: {self.__height}")
        print(f"Age: {self.__age}")


if __name__ == "__main__":
    i = 0
    my_plant = SecurePlant("Kaktus", -3, -2)
    my_plant.show_info()
    my_plant.set_age(-2)
    my_plant.set_height(-53.2)
    my_plant.show_info()
