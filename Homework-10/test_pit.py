from helpers import imports_of_your_file, height

import hashlib

try:

    import pit as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'pit.py'!"


def test_find_global_minimum(filename="pit", allowed_imports={"scipy", "scipy.optimize", "helpers"}):
    """ Checks whether find_shortest_path returns the correct shortest path."""

    found_minimum_xy = testfile.find_global_minimum()

    assert len((found_minimum_xy)), "find_global_minimum should return two values - one for x, one for y!"

    assert height(found_minimum_xy) < 0, "The lowest pit of Mordor is definitely below ground. Try again!"
    assert height(found_minimum_xy) < -50, "-50 is low, but the depths of Mordor are much deeper. Try again!"
    assert height(found_minimum_xy) < -900, "It is hard to believe, but the minimum goes lower than -900 even. Try again!"
    assert height(found_minimum_xy) < -900, "The lowest pit is deeper than -950 even. Get just a bit lower, and you shall pass this task!"
    
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import any modules except SciPy!"
