""" Script that tests the functionality of the Citrus class. """

import types

try:

    import citrus as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'citrus.py'!"


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


def test_imports(filename="citrus", allowed_imports={"random"}):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import any modules except random!"


def test_citrus():
    """ Checks Citrus class functionality. """

    a = testfile.Citrus()
    b = testfile.Citrus(species=None)

    pom = testfile.Citrus(species="Pomelo")

    assert hasattr(pom, "species"), "'Citrus' object does not have a 'species' attribute!"
    assert pom.species == "Pomelo", "'Citrus' object does not have the specified species!"

    assert str(a) == "<Citrus of species {}>".format(a.species), "'Citrus' object does not have the specified string representation!"
    assert str(pom) == "<Citrus of species Pomelo>",  "'Citrus' object does not have the specified string representation!"

    man = testfile.Citrus(species="Mandarin")
    swo = testfile.Citrus(species="Sweet Orange")
    wim = testfile.Citrus(species="Wildleaf Mandarin")
    cit = testfile.Citrus(species="Citron")
    bio = testfile.Citrus(species="Bitter Orange")

    assert isinstance(a + b, testfile.Citrus), "Crossover operation does not return 'Citrus' object!"

    assert (a + a).species == a.species, "Crossover rules are not followed in detail!"
    assert (swo + bio).species.endswith("Orange"), "Crossover rules are not followed in detail!"

    assert (pom + swo).species == "Grapefruit", "Crossover rules are not followed in detail!"
    assert (swo + wim).species == "Clementine", "Crossover rules are not followed in detail!"
    assert (cit + bio).species == "Lemon", "Crossover rules are not followed in detail!"

    try:
        a + 7
    except TypeError as e:
        assert "plant" in str(e), "You have to mention the word 'plant' at least once in the TypeError message!"

    try:
        7 + a
    except TypeError as e:
        assert "plant" in str(e), "You have to mention the word 'plant' at least once in the TypeError message!"

