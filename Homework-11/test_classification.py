from helpers import imports_of_your_file

import pickle

try:

    import classification as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'classification.py'!"


def test_find_closest_author(filename="classification", allowed_imports={"numpy", "pickle", "scipy.spatial"}):
    """ Checks whether the expected classification is given by find_closest_author. """

    with open("reference/authors_noun_synsets.pickle", "rb") as fh:
        reference = pickle.load(fh)

    with open("reference/authors_pos_freqs.pickle", "rb") as fh:
        authors_pos_freqs = pickle.load(fh)

    with open("reference/authors_noun_synsets.pickle", "rb") as fh:
        authors_noun_synsets = pickle.load(fh)

    with open("reference/a_pos_freqs.pickle", "rb") as fh:
        test_pos_freqs = pickle.load(fh)

    with open("reference/a_noun_synsets.pickle", "rb") as fh:
        test_noun_synsets = pickle.load(fh)

    a_pos = testfile.find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="pos")
    a_synsets = testfile.find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="synsets")

    assert type(a_pos) == str, "You should return the name of the author!"
    assert a_pos == "Bram Stoker", "'Bram Stoker' should be the prediction for texts/test/a.txt!"
    assert a_synsets == "Bram Stoker", "'Bram Stoker' should be the prediction for texts/test/a.txt!"

    with open("reference/b_pos_freqs.pickle", "rb") as fh:
        test_pos_freqs = pickle.load(fh)

    with open("reference/b_noun_synsets.pickle", "rb") as fh:
        test_noun_synsets = pickle.load(fh)

    b_pos = testfile.find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="pos")
    b_synsets = testfile.find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="synsets")

    assert b_pos == "Lewis Carroll", "'Lewis Carroll' should be the prediction for texts/test/b.txt!"
    assert b_synsets == "Lewis Carroll", "'Lewis Carroll' should be the prediction for texts/test/b.txt!"

    with open("reference/c_pos_freqs.pickle", "rb") as fh:
        test_pos_freqs = pickle.load(fh)

    with open("reference/c_noun_synsets.pickle", "rb") as fh:
        test_noun_synsets = pickle.load(fh)

    c_pos = testfile.find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="pos")
    c_synsets = testfile.find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="synsets")

    assert c_pos == c_synsets, "The predicted authors for both methods should be equal for texts/test/c.txt!"

    with open("reference/d_pos_freqs.pickle", "rb") as fh:
        test_pos_freqs = pickle.load(fh)

    with open("reference/d_noun_synsets.pickle", "rb") as fh:
        test_noun_synsets = pickle.load(fh)

    d_pos = testfile.find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="pos")
    d_synsets = testfile.find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="synsets")

    assert d_pos != d_synsets, "The predicted authors for both methods should be unequal for texts/test/d.txt!"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import anything but SciPy, pickle, and NumPy!"
