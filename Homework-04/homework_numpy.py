# Import NumPy here!
import numpy as np

def expomultiadditive_division(a, b, c):
    return (np.e ** (a*(b+c)))/(a**2 - b**2 + c**2) 


def strange_pattern(shape):
    """ Creates a strange pattern with shape (n x m)."""
    
    # create an array with only ones as boolean (all False)
    array = np.zeros(shape, dtype=bool)
    col = 0
    
    # for each row in the array, fill every 3rd column with True
    for row in range(array.shape[0]):
        array[row, col::3] = True
        # every 3rd row, the indexing has to start at column 0 again
        if col == 2:
            col = 0
        else:
            # each row, move one column to the right
            col += 1
            
    return array


def dimension_reduction(array):
    """ Reduces the first dimension of an array to its sum and the last dimension to its median. Returns the stddev of the array. """
    
    array = np.sum(array, axis=0)
    array = np.median(array, axis=len(array.shape)-1)
    
    return np.std(array)


def interpolate(numbers, n_steps):
    start = numbers[0]
    end = numbers[-1]
    
    return np.linspace(start, end, n_steps * (len(numbers)-1) + 1)


if __name__ == "__main__":
    # testing the functions
    pass