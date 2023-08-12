import numpy as np

def compute_rank(array):
    """
    Function for computing the ranks of an array from lowest to highest value.
    
    Args:
    - array: n-dimensional input array with arbitrary shape
    """
    
    # our ranking is the sorted list of these indices which would sort our input array
    # axis=None works with a flattened array
    # reshape back into original input array shape
    return np.argsort(np.argsort(array, axis=None)).reshape(array.shape)
    
    
    

