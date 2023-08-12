from helpers import imports_of_your_file
from pandas.testing import assert_frame_equal, assert_series_equal
import numpy as np
import pandas as pd

try:
    import to_categorical as testfile
except ModuleNotFoundError:
    assert False, 'The name of your file is supposed to be "to_categorical.py!"'


def test_to_categorical(filename='to_categorical', allowed_imports=None):

    if allowed_imports is None:
        allowed_imports = {'numpy', 'pandas', 'matplotlib.pyplot', 'pandas.core.dtypes.dtypes', 'load_data'}
    # load data
    df = pd.read_pickle('reference_data/load_data.pickle')
    # pass to function
    result = testfile.to_categorical(df['AgeGroup'])
    assert result is not None, 'Your function does not return anything'
    reference = pd.read_pickle('reference_data/to_categorical.pickle')
    assert_series_equal(reference, result)
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, 'You are not allowed to import any modules except NumPy, Pandas, pandas.core.dtypes.dtypes, Matplotlib and your load_data module'

if __name__ == '__main__':

    test_to_categorical()
    print('pass')