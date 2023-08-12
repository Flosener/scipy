""" Script that tests the first Fibonacci number that has a digit sum higher than 42. """

import hashlib
import types

try:

    import findfib as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'findfib.py'!"


def test_imports(filename="findfib", allowed_imports={"fibonacci", "digsum"}):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import modules other than 'fibonacci' and 'digsum'!"


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


def test_findfib():
    """ Checks if found number is correct by comparing against hash of correct solution. """

    assert hasattr(testfile, "findfib"), "Your Script must have an 'findfib'-function!"
    assert hashlib.sha256(str(testfile.findfib()).encode("utf-8")).hexdigest() == "8e8bf3299e38a97f508c6e339fe60f1dc5e80cfca14ab13371cd1daed8c319d1"


