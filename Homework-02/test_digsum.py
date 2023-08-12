""" Script that tests digit sum functionality. """

import types

try:

    import digsum as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'digsum.py'!"


def test_imports(filename="digsum", allowed_imports=set()):
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


def test_digsum():
    """ Checks digit sum functionality. """

    assert hasattr(testfile, "digsum"), "Your Script must have an 'digsum'-function!"

    assert testfile.digsum(0) == 0
    assert testfile.digsum(9) == 9
    assert testfile.digsum(12) == 3
    assert testfile.digsum(333) == 9
    assert testfile.digsum(9173) == 20
    assert testfile.digsum(12345) == 15


