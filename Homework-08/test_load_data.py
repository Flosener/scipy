from helpers import imports_of_your_file
from pandas.testing import assert_frame_equal, assert_series_equal

import numpy as np
import pandas as pd

try:
    import load_data as testfile
except ModuleNotFoundError:
    assert False, 'The name of your file is supposed to be "load_data.py!"'


def test_load_data(filename='load_data', allowed_imports=None):

    if allowed_imports is None:
        allowed_imports = {'numpy', 'pandas', 'matplotlib.pyplot', 'pandas.core.dtypes.dtypes'}

    result = testfile.load_data()
    assert result is not None, 'Your function does not return anything'
    reference = pd.read_pickle('reference_data/load_data.pickle')
    assert_frame_equal(reference, result)
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, 'You are not allowed to import any modules except NumPy, Pandas, pandas.core.dtypes.dtypes and Matplotlib!'

