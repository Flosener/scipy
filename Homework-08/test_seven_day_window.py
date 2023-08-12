from helpers import imports_of_your_file
from pandas.testing import assert_frame_equal, assert_series_equal
import numpy as np
import pandas as pd

try:
    import seven_day_window as testfile
except ModuleNotFoundError:
    assert False, 'The name of your file is supposed to be "seven_day_window.py!"'


def test_seven_day_window(filename='seven_day_window', allowed_imports=None):

    if allowed_imports is None:
        allowed_imports = {'numpy', 'pandas', 'matplotlib.pyplot', 'pandas.core.dtypes.dtypes', 'load_data'}
    # load data
    df = pd.read_pickle('reference_data/load_data.pickle')
    result = testfile.seven_day_window(df)
    assert result is not None, 'Your function does not return anything'
    reference = pd.read_pickle('reference_data/seven_day_window.pickle')
    assert_frame_equal(reference, result)
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, 'You are not allowed to import any modules except NumPy, Pandas, pandas.core.dtypes.dtypes, Matplotlib and your load_data module'


if __name__ == '__main__':

    test_seven_day_window()
    print('pass')