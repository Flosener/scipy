from helpers import imports_of_your_file

import numpy as np
import pandas as pd
from hashlib import sha1


try:
    import pokemon as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'pokemon.py'!"


def test_pokemon(filename="pokemon", allowed_imports={'numpy', 'pandas'}):

    df = pd.read_csv('Pokemon_no_duplicates.csv', index_col=0)

    result = testfile.most_common(df)

    assert type(result) == str, 'Your function should return a string'
    assert result == 'Braviary', 'The returned name for the whole dataset is incorrect'

    # test with subset
    df = df[df['Type 1'] != 'Normal']
    result = testfile.most_common(df)
    assert sha1(result.encode('utf-8')).hexdigest() == '0ec7e35aedecff84adc9feb276425e5e660f0e3f', 'The name for a subset of the data is incorrect'

    # test with subset
    df = df[df['Type 2'] != 'Poison']
    result = testfile.most_common(df)
    assert sha1(result.encode('utf-8')).hexdigest() == 'b6f4d8388dec62a03fa4f7f734bb436d1268cdae', 'The name for a subset of the data is incorrect'


    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, 'You are not allowed to import any modules except NumPy and Pandas!'
