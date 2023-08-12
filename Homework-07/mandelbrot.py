from helpers import mandelbrot

import matplotlib.pyplot as plt
import numpy as np


def main():

    fig, ax = visualize_mandelbrot()

    plt.tight_layout()

    plt.show()


def visualize_mandelbrot():
    """ Visualizes the Mandelbrot Set in a rectangle spanning from (-1.5, 1.0) in the top left corner to (0.5, -1.0) in the bottom right corner. """

    # write your code here

    raise NotImplementedError


if __name__ == "__main__":
    main()
