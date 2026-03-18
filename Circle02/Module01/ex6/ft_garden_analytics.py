class Plant:
    def __init__(self, name: str, height: float):
        self.__name = name
        self.__height = 0.0

        self.set_height(height)
    # SET VALUES

    def set_height(self, height: float):
        if (self.checker(self.__height)):
            self.__height = height

    def set_name(self, name: str):
        self.__name = name
    # GET VALUES

    def get_height(self):
        return self.__height

    def get_name(self):
        return self.__name
    # CHECKER

    def checker(self, height: float):
        if (height < 0.0):
            print("Error, height cannot be negative")
            return 0
        return 1

    def get_info(self):
        print(f"{self.__name}: {self.__height}cm")

    def grow(self):
        self.__height += 1


def show_header():
    print("=== Garden Management System Demo ===\n")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: float, color: str, bloom: bool):
        super().__init__(name, height)
        self.__color = color
        self.__bloom = bloom

    def get_color(self):
        return self.__color

    def get_bloom(self):
        return self.__bloom

    def set_color(self, color: str):
        self.__color = color

    def set_bloom(self, bloom: bool):
        self.__bloom = bloom

    def get_info(self):
        if (self.__bloom):
            print(f"{self.get_name()}: {self.get_height()}cm,\
        {self.get_color()} flowers (blooming)")
        else:
            print(f"{self.get_name()}: {self.get_height()}cm,\
        {self.get_color()} flowers")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: float, color: str, bloom: bool,
                 prize: int):
        super().__init__(name, height, color, bloom)
        if (prize >= 0):
            self.__prize = prize
        else:
            self.__prize = 0

    def get_prize(self):
        return self.__prize

    def set_prize(self, prize: int):
        if (prize >= 0):
            self.__prize = prize
        else:
            print("Prize cannot be less than 0 !")

    def get_info(self):
        if (self.get_bloom()):
            print(f"{self.get_name()}: {self.get_height()}cm,\
 {self.get_color()} flowers (blooming), Prize points: {self.get_prize()}")
        else:
            print(f"{self.get_name()}: {self.get_height()}cm,\
        {self.get_color()} flowers, Prize points: {self.get_prize()}")


class Garden:
    def __init__(self, name: str):
        self.__name = name
        self.__tab_plants = [0] * 100
        self.__nb_plant = 0
        self.__total = 0
        self.__nb_plants = 0
        self.__nb_flower = 0
        self.__nb_flowerprize = 0

    def get_name(self):
        return self.__name

    def get_nb_plant(self):
        return self.__nb_plant

    def get_nb_plants(self):
        return self.__nb_plants

    def get_flower(self):
        return self.__nb_flower

    def get_flower_prize(self):
        return self.__nb_flowerprize

    def add_plant(self, plant: Plant):
        self.__tab_plants[self.get_nb_plant()] = plant
        self.__nb_plant += 1
        print(f"Added {plant.get_name()} to {self.get_name()}'s garden")
        if (plant.__class__.__name__ == "Plant"):
            self.__nb_plants += 1
        elif (plant.__class__.__name__ == "FloweringPlant"):
            self.__nb_flower += 1
        else:
            self.__nb_flowerprize += 1

    def watercan(self):
        print(f"{self.get_name()} is helping all plants grow...")
        for i in range(0, self.__nb_plant):
            self.__tab_plants[i].grow()
            self.__total += 1
            print(f"{self.__tab_plants[i].get_name()} grew 1cm")

    def calculate_score(self):
        score = 0
        for i in range(0, self.__nb_plant):
            score += self.__tab_plants[i].get_height()
            class_name = self.__tab_plants[i].__class__.__name__
            if (class_name == "PrizeFlower"):
                score += self.__tab_plants[i].get_prize()
            if (class_name == "PrizeFlower" or class_name == "FloweringPlant"):
                if (self.__tab_plants[i].get_bloom()):
                    score += 10
        return score

    def test_height(self):
        for i in range(0, self.__nb_plant):
            if (self.__tab_plants[i].get_height() < 0):
                return 0
        return 1

    def get_info(self):
        print(f"=== {self.get_name().capitalize()}'s Garden Report ===")
        print("Plants in the garden:")

        for i in range(0, self.__nb_plant):
            print("- ", end="")
            self.__tab_plants[i].get_info()

        print(f"Plants added: {self.get_nb_plant()}, \
 Total growth: {self.__total}cm")

        print(f"Plant types: {self.get_nb_plants()} regular, "
              f"{self.get_flower()} flowering, "
              f"{self.get_flower_prize()} prize flowers")


class GardenStats:
    def __init__(self):
        self.nb_plant = 0
        self.nb_flower = 0
        self.nb_flowerprize = 0


class GardenManager:
    def __init__(self):
        self.tab_garden = [0] * 10
        self.nb_garden = 0
        self.stats = GardenStats()

    def test_height(self):
        for i in range(0, self.nb_garden):
            if (self.tab_garden[i].test_height() == 0):
                print("Height validation test: False")
                return 0
        print("Height validation test: True")

    def get_info(self):
        print("Garden scores - ", end="")

        for i in range(0, self.nb_garden):
            print(f"{self.tab_garden[i].get_name()}: "
                  f"{self.tab_garden[i].calculate_score()}", end="")
            if (i != (self.nb_garden - 1)):
                print(",", end=" ")
            else:
                print(".")
        print(f"Total gardens managed: {self.nb_garden}")

    def add_garden(self, garden: Garden):
        self.tab_garden[self.nb_garden] = garden
        self.nb_garden += 1

    def get_stats(self):
        self.stats.nb_flower = 0
        self.stats.nb_plant = 0
        self.stats.nb_flowerprize = 0

        i = 0
        for i in self.tab_garden[i]:
            garden = self.tab_garden[i]
            self.stats.nb_flower += garden.get_nb_flower()
            self.stats.nb_flowerprize += garden.get_nb_flowerprize()
            self.stats.nb_plant += garden.get_nb_plants()


if __name__ == "__main__":
    show_header()
    my_plants = [
        FloweringPlant("Rose", 25.0, "red", 1),
        Plant("Oak", 450.5),
        PrizeFlower("Tomato", 80.0, "red", 1, 10),
        Plant("PalmTree", 300.5)
    ]

    my_gardens = [
        Garden("Tomek"),
        Garden("Julia")
    ]

    network = GardenManager()

    network.add_garden(my_gardens[0])
    network.add_garden(my_gardens[1])

    my_gardens[0].add_plant(my_plants[0])
    my_gardens[0].add_plant(my_plants[1])
    my_gardens[1].add_plant(my_plants[2])
    my_gardens[1].add_plant(my_plants[3])

    print("")

    my_gardens[1].watercan()

    print("")

    my_gardens[1].get_info()

    print("")

    network.test_height()
    network.get_info()
