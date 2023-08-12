""" Script that tests the functionality of the Garden class. """

import types

try:

    import garden as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'garden.py'!"


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


def test_imports(filename="garden", allowed_imports={"random", "citrus"}):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import any modules except random and Citrus!"


def test_garden():
    """ Checks Garden class functionality. """

    g = testfile.Garden()

    assert hasattr(g, "plants"), "'Garden' object does not have a 'plants' attribute!"
    assert g.plants == [], "Attribute 'plants' is not initialized as empty list!"

    for _ in range(5_000):
        g.plant()

    assert len(g) == 5_000, "len() does not return the expected length!"
    assert len(g) == len(g.plants), "len() does not return the correct length!"

    assert str(g).startswith("<Garden with ") and str(g).endswith(" species>"), "'Garden' object does not have the specified string representation!"
    assert int(str(g)[13:-9].split(" plants and ")[0]) == len(g), "'Garden' object does not have the specified string representation!"
    assert int(str(g)[13:-9].split(" plants and ")[1]) == 3, "Either something very unlikely just happened or you have an error. Try again!"

    for _ in range(15_000):
        g.cross()

    assert len(g) == 20_000, "Crossover did not change length in expected way!"
    assert int(str(g)[13:-9].split(" plants and ")[1]) == 11, "Either something very unlikely just happened or you have an error. Try again!"

