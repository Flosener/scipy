""" Script that tests Fibonacci functionality. """

import types

try:

    import fibonacci as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'fibonacci.py'!"


def test_imports(filename="fibonacci", allowed_imports=set()):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import other modules in this exercise!"


def imports_of_your_file(filename):
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


def test_fibonacci():
    """ Checks Fibonacci functionality. """

    assert hasattr(testfile, "fibonacci"), "Your Script must have an 'fibonacci'-function!"

    assert testfile.fibonacci(0) == 0
    assert testfile.fibonacci(1) == 1
    assert testfile.fibonacci(2) == 1
    assert testfile.fibonacci(3) == 2
    assert testfile.fibonacci(6) == 8
    assert testfile.fibonacci(10) == 55
    assert testfile.fibonacci(12) == 144
    assert testfile.fibonacci(20) == 6765
    assert testfile.fibonacci(30) == 832040

