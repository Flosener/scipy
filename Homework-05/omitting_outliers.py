import numpy as np

def remove_outliers(data, m=3, replace=True):
    """
    Function that removes outliers from given data.
    
    Args:
    - data: n-dimensional input array
    - m: factor for threshold calculation (default = 3)
    - replace: boolean that determines whether outliers are replaced by the mean of input array or deleted (default = True)
    """
    
    # calculate mean, stddev and threshold for outliers
    mean = np.mean(data)
    sigma = np.std(data)
    threshold = m * sigma
    array = np.ndarray.copy(data)
    
    if(replace):
        # if flag is True, replace all outliers by the array's mean
        array[np.abs(array - mean) > threshold] = mean
        return array
    else:
        # else return a 1D array with removed outliers
        return array[np.abs(array - mean) <= threshold]

