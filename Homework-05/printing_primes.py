from helpers import is_prime, pretty_print_bool_array

import numpy as np

# convert function to numpy ufunc to work with numpy arrays
is_prime_numpy = np.vectorize(is_prime)

def print_primes(rows, cols):
    """
    Function to print prime numbers in a rows by cols array.
    
    Args:
    - rows: number of rows
    - cols: numbers of columns
    """
    # create rows * cols boolean array with size rows*cols
    array = np.arange(rows*cols).reshape(rows,cols)
    ix_row, ix_col = np.indices((rows,cols))
    
    # print the resulting pretty prime array
    pretty_print_bool_array(is_prime_numpy(array[ix_row, ix_col]))