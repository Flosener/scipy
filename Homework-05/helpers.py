import numpy as np

import types

def is_prime(n):
    """simple function to check if a given integer is prime"""
    # no change necessary here

    if n <= 1:
        return False

    if n > 2 and n % 2 == 0:
        return False

    for i in range(3, int(np.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def pretty_print_bool_array(array):
    """this function will print a boolean array such that True values are 'x'
    and False values are '.'"""

    with np.printoptions(formatter={"bool": lambda b: "x" if b else "."}):
        print(array)


def imports_of_your_file(filename, testfile):
    """ Yields all imports in the testfile. """

    for name, val in vars(testfile).items():
        if isinstance(val, types.ModuleType):
            # get direct imports
            yield val.__name__

        else:
            # get from x import y imports
            imprt = getattr(testfile, name)

            if hasattr(imprt, "__module__") and not str(imprt.__module__).startswith("_") and not str(imprt.__module__) == filename:
                yield imprt.__module__

