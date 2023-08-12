from helpers import imports_of_your_file

import pickle

try:

    import synsets as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'synsets.py'!"


def test_get_noun_synsets(filename="synsets", allowed_imports={"spacy", "numpy", "nltk", "nltk.corpus.reader.wordnet"}):
    """ Checks whether get_noun_synsets returns the correct synsets. """

    with open("reference/authors_noun_synsets.pickle", "rb") as fh:
        reference = pickle.load(fh)["Lewis Carroll"]

    returned = testfile.get_noun_synsets("texts/train/alice_in_wonderland.txt")

    assert type(returned) == set, "You should return a set of synsets!"
    assert type(list(returned)[0]) == str, "The synsets should be represented by their name!"
    assert len(returned) == 113, "There should be 113 synsets for Alice in Wonderland!"
    assert returned == reference, "The returned synsets are not the same as the reference synsets!"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import anything but spaCy, nltk, and NumPy!"
