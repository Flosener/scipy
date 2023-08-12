from scipy import spatial

import numpy as np

import pickle


def main():

    # load authors pos freqs
    with open("reference/authors_pos_freqs.pickle", "rb") as fh:
        authors_pos_freqs = pickle.load(fh)

    # load authors noun synsets
    with open("reference/authors_noun_synsets.pickle", "rb") as fh:
        authors_noun_synsets = pickle.load(fh)

    # load test pos freqs
    with open("reference/a_pos_freqs.pickle", "rb") as fh:
        test_pos_freqs = pickle.load(fh)

    # load test noun synsets
    with open("reference/a_noun_synsets.pickle", "rb") as fh:
        test_noun_synsets = pickle.load(fh)

    # predict test author based on pos freqs
    pred_author = find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="pos")
    print("Method 'pos' predicts '{}' for file texts/test/a.txt.".format(pred_author))

    # predict test author based on noun synsets
    pred_author = find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="synsets")
    print("Method 'synsets' predicts '{}' for file texts/test/a.txt.".format(pred_author))

    # print true author
    print("The true author of file texts/test/a.txt is 'Bram Stoker'.")


def find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="pos"):

    raise NotImplementedError
    

if __name__ == "__main__":
    main()
