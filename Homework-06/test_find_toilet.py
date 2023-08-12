from helpers import imports_of_your_file

import numpy as np
import pandas as pd
from hashlib import sha1


try:
    import find_toilet as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'find_toilet.py'!"


def test_find_toilet(filename='find_toilet', allowed_imports={'numpy', 'pandas'}):

    lat, lon = -32.908042, 150.596883
    result = testfile.find_closest_toilet(lat, lon)
    result[-1] = np.rint(result[-1])
    expected = np.array([4478, 'Denman Recreational Area', 150.67386603, - 32.38491785, 59.0]).astype(str)
    assert result.values.shape == expected.shape, 'Your result has the wrong shape'

    result = result.values.astype(str)
    assert np.all(result == expected), 'Your function returns an incorrect result'

    lat, lon = -32.492425, 116.284233
    result = testfile.find_closest_toilet(lat, lon)
    # round for identical hash
    result[-1] = np.rint(result[-1])
    result = result.values.astype(str)
    assert sha1(str(result).encode('utf-8')).hexdigest() == '6038d5a7119ba70de12b584c519ae5eddd0f9118', 'Your function returns an incorrect result'

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, 'You are not allowed to import any modules except NumPy and Pandas!'