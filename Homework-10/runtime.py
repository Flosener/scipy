from scipy import spatial
from scipy import integrate

import numpy as np


def main():

    print("The way from The Shire to Rivendell should take about 186 hours:") 
    print(calculate_runtime((355, 455), (697, 418)))


def calculate_runtime(start_coords, target_coords):

    # get euclidean distance matrix
    distance = spatial.distance.euclidean(start_coords, target_coords)
    
    # define decay lambda function
    pace_fct = lambda s: 1.015**s
    
    # calculate runtime by integrating over our pace function with 0 as lower, distance as upper bound
    runtime = integrate.quad(pace_fct, 0, distance)
    
    # return runtime in hours
    return runtime[0]/60


if __name__ == "__main__":
    main()
