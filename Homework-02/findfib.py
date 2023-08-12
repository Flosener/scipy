""" Script that finds the first Fibonacci number that has a digit sum higher than 42. """

from fibonacci import fibonacci
from digsum import digsum

def main():

    print("findfib() returns", findfib())


def findfib():
    """ This function returns the first Fibonacci number that has a digit sum higher than 42. """
    counter = 0
    fib = 0
    
    while digsum(fib) <= 42:
        fib = fibonacci(counter)
        counter += 1
    
    return fib


if __name__ == "__main__":
    main()
