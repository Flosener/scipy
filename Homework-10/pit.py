from helpers import height

from scipy import optimize


BOUNDS = (
    (-512, 512), # min, max for x
    (-512, 512)  # min, max for y
)


def main():
    
    found_minimum_xy = find_global_minimum()

    print("These are the coordinates of the found minimum:")
    print(found_minimum_xy)

    print("This is the height at the found minimum:")
    print(height(found_minimum_xy))
    

def find_global_minimum():

    raise NotImplementedError
    


if __name__ == "__main__":
    main()
