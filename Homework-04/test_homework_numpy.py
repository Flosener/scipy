from hashlib import sha1

import numpy as np
import types

try:
    import homework_numpy as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is suppoesed to be 'homework_numpy.py'!"

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


def test_imports(filename="homework_numpy", allowed_imports={"numpy"}):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import any modules except NumPy!"


def test_expomultiadditive_division():
    a = 0.1
    b = -0.25
    c = 0.42

    result = testfile.expomultiadditive_division(a, b, c)
    rounded = np.int32(result)

    assert sha1(rounded).hexdigest() == 'a454ca483b4a66b83826d061be2859dd79ff0d6c', "Your function does not produce the correct result!"

    a = 0.1
    b = np.linspace(-0.5, 0.5, 100)
    c = np.linspace(-2, 2, 100 * 100).reshape(100, 100)

    try:
        testfile.expomultiadditive_division(a, b, c)

    except ValueError:
        assert False, "Your function does not support broadcasting!"


def test_strange_pattern():
    result = testfile.strange_pattern((10, 10))

    assert type(result) is np.ndarray, "Your function does not return a NumPy array!"
    assert result.dtype is np.dtype("bool"), "Your function does not return a boolean array!"
    assert sha1(result).hexdigest() == '4c41d4d448bdfa8f8986940fb2c79df8c80e28d8', "Your function does not produce the correct pattern!"

    result = testfile.strange_pattern((2, 2))

    assert sha1(result).hexdigest() == "0ad4fab2096b1e998cd969538602507d07fd5e4c", "Your function does not produce the correct pattern in an edge case!"

    result = testfile.strange_pattern((0, 0))

    assert result.shape == (0, 0), "Your function does not produce the correct pattern in an edge case!"


def test_dimension_reduction():
    array = np.arange(9).reshape(3, 3)
    result = testfile.dimension_reduction(array)

    assert result == 0, "Your function does not return the correct result!"

    array = np.arange(27).reshape(3, 3, 3)
    result = testfile.dimension_reduction(array)
    rounded = np.int32(result)

    assert sha1(rounded).hexdigest() == '2f086fc767a0dac59a38c67f409b4f74a1eab39f', "Your function does not produce the correct result!"


def test_interpolate():
    numbers = [0, 1]
    n_steps = np.random.randint(10, 100)

    result = testfile.interpolate(numbers, n_steps)

    assert np.allclose(result, np.linspace(0, 1, n_steps + 1)), "Your function does not produce the correct result!"

    numbers = list(range(0, 100, 10))
    n_steps = 5

    result = testfile.interpolate(numbers, n_steps)

    assert np.allclose(result, np.arange(0, 91, 2)), "Your function does not produce the correct result!"
