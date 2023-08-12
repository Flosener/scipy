from helpers import imports_of_your_file

import hashlib

try:

    import runtime as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be `runtime.py'!"


def test_calculate_runtime(filename="runtime", allowed_imports={"scipy", "scipy.integrate", "scipy.spatial", "numpy"}):
    """ Checks whether find_shortest_path returns the correct shortest path."""

    assert type(testfile.calculate_runtime((355, 455), (697, 418))) == float, "calculate_runtime should return a float!"

    assert int(testfile.calculate_runtime((355, 455), (697, 418))) == 186, "The runtime between The Shire and Rivendell should be about 186 hours!"
    assert int(testfile.calculate_runtime((970, 915), (1073, 876))) == 4, "The runtime between Minas Morgul and Mount Doom should be about 4 hours!"

    shire_isengard_runtime = testfile.calculate_runtime((355, 455), (626, 741))
    assert hashlib.sha256(str(shire_isengard_runtime).encode("utf-8")).hexdigest() == "651293d7e435933e6d8ac86f931b94abe36946fcdd0e095c9bdf88ea98c7739b", "The runtime between The Shire and Isengard is incorrect!"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import any modules except NumPy and SciPy!"
