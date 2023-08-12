""" Script that provides Fibonacci functionality. """

def main():

    print("fibonacci(0) =", fibonacci(0))
    print("fibonacci(3) =", fibonacci(3))
    print("fibonacci(10) =", fibonacci(10))


def fibonacci(n):
    """ This function returns the nth Fibonacci number given that fibonacci(0) = 0. """
    fib_sequence = list(range(n+1)) # n+1 because list(range(x)) starts at 0; numbers serve as placeholder
    
    for index, fib_number in enumerate(fib_sequence):
        if index <= 1:
            pass # Fn-1 = 0 and Fn-2 = 1 anyways
        else:
            fib_sequence[index] = fib_sequence[index-1] + fib_sequence[index-2]
        
    return fib_sequence[-1] # return last fibonacci number


if __name__ == "__main__":
    main()
