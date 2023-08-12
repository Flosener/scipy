from helpers import imports_of_your_file

from hashlib import sha1
from io import StringIO

import numpy as np

import sys

try:
    import printing_primes as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'printing_primes.py'!"


def test_print_primes(filename="printing_primes", allowed_imports={"numpy", "helpers"}):

    assert callable(testfile.is_prime_numpy), "Your script does not have a function 'is_prime_numpy'"

    try:
        testfile.is_prime_numpy(np.arange(3))
    except ValueError:
        assert False, "Your 'is_prime_numpy' function does not seem to be able to handle NumPy arrays"

    test_stdout = StringIO()
    saved_stdout = sys.stdout

    sys.stdout = test_stdout

    result = testfile.print_primes(20, 20)

    sys.stdout = saved_stdout

    s = test_stdout.getvalue()

    assert result is None, "Your function 'print_primes' should not have a return value"
    assert len(s) > 0, "Your function 'print_primes' should *print* its result!"
    assert sha1(s.encode("utf-8")).hexdigest() == "3c49338521ff33568de33bdeb89ae5b83a5b6c45", "Your function 'print_primes' does not seem to print the correct result"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import any modules except NumPy and helpers.py!"

