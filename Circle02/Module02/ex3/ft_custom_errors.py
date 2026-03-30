class GardenError(Exception):
    """OTHER GARDEN ERROR"""
    pass


class PlantError(GardenError):
    """PLANT IS DOING BADLY"""
    pass


class WaterError(GardenError):
    """NOT ENOUGH WATER IN THE TANK"""
    pass


class Plant:
    def __init__(self, name: str, water: float, sun: int):
        self.__name = name
        self.__water = water
        self.__sun = sun

    # GET VALUES

    def get_water(self):
        return self.__water

    def get_sun(self):
        return self.__sun

    def get_name(self):
        return self.__name

    def test_water(self):
        if (self.get_water() < 10):
            raise WaterError("Not enough water in the tank!")
        else:
            print(f"Enough literes of water in the tank: {self.get_water()}")

    def test_sun(self):
        if (self.get_sun() > 100):
            raise PlantError(f"The {self.get_name()} plant is wilting!")
        elif (self.get_sun() < 50):
            raise PlantError(f"The {self.get_name()} is not getting\
 enough sun!")
        else:
            print(f"The {self.get_name()} is taking in the sun!")


def checker(plant: Plant):
    print("=== Custom Garden Errors Demo ===\n")
    errors: list[GardenError] = []
    print(f"Testing {PlantError.__name__}...")
    try:
        plant.test_sun()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
        errors.append(e)
    print(f"Testing {WaterError.__name__}...")
    try:
        plant.test_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
        errors.append(e)

    print("Testing catching all garden errors...")
    for i, error in enumerate(errors, 1):
        print(f"Caught {GardenError.__name__}: {error}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    my_plant: Plant = Plant("Tomato", 9, 101)
    checker(my_plant)
