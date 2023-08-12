from helpers import imports_of_your_file

from hashlib import sha1

import numpy as np

try:
    import omitting_outliers as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'omitting_outliers.py'!"


def test_remove_outliers(filename="omitting_outliers", allowed_imports={"numpy"}):
    data = np.array([[-2,  1,  1,  0,  2, -1,  1, -3, -3, -2, -3, -3,-42,  1,  2,  1,  0,  1, -1, -1],
                     [-2, -3,  2,  2, -3, 42,  0,  2,  0, -1, -3,  1,  2,  1, -3,  0,  0, -2,  0,  1]])

    data = data.astype(float)

    result = testfile.remove_outliers(data)

    assert result.shape == data.shape, "If replace is True, your function should preserve the shape of the array"
    assert sha1(result).hexdigest() == "52ffe05d09dbe4135e1a1a16e113a1a578775a56", "Your function does not seem to return the correct result"

    result = testfile.remove_outliers(data, m=4.4)

    assert sha1(result).hexdigest() == "15e350705c1a1d2b9a8cb16b0cf05b2266a9a2fd", "Your function does not seem to return the correct result"

    result = testfile.remove_outliers(data, replace=False)

    assert result.shape == (38, ), "If replace is False, your function should reduce the number of elements"
    assert sha1(result).hexdigest() == "c51ef6b5de6a9654dcf2d4f69de324eb2591cac6", "Your function does not seem to return the correct result"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import any modules except NumPy!"

