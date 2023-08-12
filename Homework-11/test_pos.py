from helpers import imports_of_your_file

import numpy as np

import pickle
import spacy

try:

    import pos as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'pos.py'!"


def test_get_pos_freqs(filename="pos", allowed_imports={"spacy", "numpy"}):
    """ Checks whether get_pos_freqs returns the correct frequencies. """

    with open("reference/authors_pos_freqs.pickle", "rb") as fh:
        reference = pickle.load(fh)["Lewis Carroll"]

    returned = testfile.get_pos_freqs("texts/train/alice_in_wonderland.txt")

    assert type(returned) == np.ndarray, "You should return a np.ndarray of frequencies!"
    assert returned.shape == (len(spacy.parts_of_speech.IDS),), "The returned POS frequencies do not have the correct shape!"
    assert np.allclose(returned, reference), "The returned POS frequencies are not the same as the reference POS frequencies!"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import any modules except spaCy and NumPy!"
