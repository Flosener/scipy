from helpers import imports_of_your_file

from hashlib import sha1

import numpy as np
import pandas as pd

try:
    import countries as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'countries.py'!"


def test_countries(filename="countries", allowed_imports={"numpy", "pandas"}):

    data_shape = (2, 4)
    result = testfile.aggregate_european_countries()
    assert result is not None, 'Your function does not return anything'
    assert result.values.shape == data_shape, "Your dataframe has an incorrect shape"

    assert sha1(str(result.values).encode("utf-8")).hexdigest() == 'c69625c1338c996857c3f75c1020b464c47a7075', "Your function does not seem to return the correct result"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import any modules except NumPy and Pandas!"
