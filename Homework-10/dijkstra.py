from scipy import spatial
from scipy import sparse

import numpy as np

INDEX = (
    "The Shire",
    "Rivendell",
    "Misty Mountains",
    "Isengard",
    "Helm's Deep",
    "Minas Tirith",
    "Minas Morgul",
    "Mount Doom"
)

COORDS = (
    (355, 455),
    (697, 418),
    (670, 566),
    (626, 741),
    (663, 800),
    (944, 915),
    (970, 915),
    (1073, 876)
)


def main():

    print("This should be ['The Shire', 'Isengard', 'Minas Morgul', 'Mount Doom']:")
    print(find_shortest_path("The Shire", "Mount Doom"))


def find_shortest_path(start, target):

    # create distance matrix for all places
    dist_matrix = spatial.distance_matrix(x=COORDS,y=COORDS)
    
    # direct reach exceptions
    dist_matrix[0,5] = np.inf
    dist_matrix[0,6] = np.inf
    dist_matrix[1,5] = np.inf
    dist_matrix[1,6] = np.inf
    dist_matrix[0:6,7] = np.inf
    
    # create predecessors matrix
    shortest_dist = sparse.csgraph.dijkstra(dist_matrix, return_predecessors=True)[1]
    
    # new list to append place names
    shortest_path = []
    
    while start != target:
        shortest_path.append(target)
        last_place = shortest_dist[INDEX.index(start), INDEX.index(target)] # get index of place before
        target = INDEX[last_place] # back to string
        
    # append starting place
    shortest_path.append(start)
    
    # print resulting shortest path
    return list(reversed(shortest_path))


if __name__ == "__main__":
    main()
