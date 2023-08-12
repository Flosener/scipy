from helpers import imports_of_your_file

import numpy as np

try:
    import rigorous_ranking as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'rigorous_ranking.py'!"


def test_compute_rank(filename="rigorous_ranking", allowed_imports={"numpy"}):

    data = np.random.choice(100, size=(5, 5), replace=False)
    rank = testfile.compute_rank(data)

    assert rank.shape == data.shape, "The returned array does not have the same shape as the input array"
    assert np.array_equal(np.sort(np.unique(rank)), np.arange(rank.size)), "The returned array contains invalid values for a rank"
    assert np.array_equal(data.argsort(), rank.argsort()), "The returned array does not contain the correct ranks"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import any modules except NumPy!"

