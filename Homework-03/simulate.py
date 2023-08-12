""" Script to simulate a garden full of citrus plants. """

from garden import Garden
from citrus import Citrus


def main():

    print("\n" + "#" * 20, "Simulating Citrus", "#" * 20) 
    simulate_citrus()

    print("\n" + "#" * 20, "Simulating Garden", "#" * 20) 
    simulate_garden()


def simulate_citrus():
    """ Simulates instances of class Citrus. """

    print("\nCreating a Citrus my_citrus ...")
    my_citrus = Citrus()

    print("\nPrinting my_citrus...")
    print(my_citrus)

    print("\nCreating a Citrus other_citrus ...")
    other_citrus = Citrus()

    print("\nPrinting other_citrus ...")
    print(other_citrus)

    print("\nPrinting my_citrus + other_citrus ...")
    print(my_citrus + other_citrus)


def simulate_garden():
    """ Simulates an instance of class Garden. """

    print("\nCreating a Garden my_garden ...")
    my_garden = Garden()

    print(my_garden)

    print("\nPlanting 5 Citrus plants ...")
    for _ in range(5):
        my_garden.plant()

    print(my_garden)

    print("\nCrossing plants in my_garden 20 times ...")
    for _ in range(20):
        my_garden.cross()

    print(my_garden)

    print("\nThe following species now exist in the garden:", {plant.species for plant in my_garden.plants}, "\n")


if __name__ == "__main__":
    main()
