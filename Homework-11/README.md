# Homework 11

## Deadline: Monday, 28th of June at 00:00 (2021-06-28 00:00:00 UTC+2)

This week's homework is all about natural language processing.

Before you start, make sure your conda environment is activated and that you have installed all the packages listed in `requirements.txt` (e.g. with `pip install -r requirements.txt`).  

We will be using `spacy` and `nltk` this week, which require a bit more attention to set up and can be tricky to get to work. If you run into any errors while running `pip install -r requirements.txt`, follow these steps:

1. Try upgrading `pip` with `pip install --upgrade pip`
2. Try running just `pip install numpy==1.19.5` (if `numpy` is not already installed)
3. Try running just `pip install Cython==0.29.23` (if `Cython` is not already installed)
4. Try installing `wheel` with `pip install wheel`
5. Try installing `setuptools` with `pip install setuptools`
6. Finally, try runnning `pip install -r requirements.txt` again

When the installation of all requirements was successful, run the following two commands to download necessary resources for `spacy` and `nltk`:

```
python -c "import nltk; nltk.download('wordnet')"
python -m spacy download en_core_web_sm
```

Congratulations, you are all set up!

## Overview

There are 3 tasks in this homework:

* `pos.py`: Create a frequency vector of POS tags in a text
* `synsets.py`: Create a set of WordNet synsets of the `n` most frequent nouns in a text
* `classification.py`: Classify which author wrote a text based on POS tag frequencies and noun synsets

In order for us to try out our code on real-life examples, there are four well-known texts in [`texts/train/`](texts/train/). Their copyright has lapsed, so the `txt` files are freely available on the internet. The four texts are:

* *1984* by George Orwell (1949)
* *Alice in Wonderland* by Lewis Carroll (1864)
* *Dracula* by Bram Stoker (1897)
* *Frankenstein* by Mary Shelley (1818)

The last three chapters from each text were removed and put into [`texts/test/`](texts/test/) for testing purposes.

## Task 1: POS Frequencies

Write a function `get_pos_freqs(filepath)` in `pos.py` that returns a `np.ndarray` containing the normalized frequencies of POS tags in a text. The corresponding tag order should be the same as in `spacy.parts_of_speech.IDS.keys()`, with missing POS tags being assigned a frequency of zero. The frequencies are normalized in the sense that they should add up to `1.00`.

You can follow these steps to do that:

1. Load the text from the file in `filepath`
2. Process the whole text with `spacy`
3. Count how often each POS tag occurs
4. Sort the counts in the correct order and fill up with zeros
5. Normalize the counts (divide by total sum)
6. Return the normalized frequencies as an `np.ndarray`

This POS frequency vector can be seen as a representation of the author's style based on syntactic features. Is the author describing everything in detail with many adjectives? Or is the author more like Hemingway, known for his sparse and rather direct style?

## Task 2: Noun Synsets

Write a function `get_noun_synsets(filepath)` in `synsets.py` that returns a `set` of all WordNet synset names associated with the ten most frequent nouns in a text. 

You can follow these steps to do that:

1. Load the text from the file in `filepath`
2. Process the whole text with `spacy`
3. Get the lemmas of the tokens with POS `NOUN`
4. Select the ten most frequent noun lemmas
5. Get their corresponding synsets with `nltk`
6. Collect the names of all synsets
7. Return the `set` of synset names

This set of synset names can be seen as a representation of the author's subject matter. What's the story about? You won't find character names in there, but abstract concepts that are alluded to in the text. You will also quite a few concepts that have nothing to do with the text and just happen to be one of the meanings a common word can take on.

## Task 3: Authorship Classification

This task builds on the preprocessing done in Task 1 and Task 2, but all data is loaded from pickled files in `reference/`, so you can solve it on its own as well. 

Authorship classification, also called *authorship attribution* or more broadly [stylometry](https://en.wikipedia.org/wiki/Stylometry), is the task of determining which author composed a given text. We will use a very simple [nearest-neighbor classification](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) approach to find out which of the four authors George Orwell, Lewis Caroll, Bram Stoker, and Mary Shelley composed each of the extracted chapters in [`texts/test/`](texts/test/).  

For that purpose, we will compute the distance between a given chapter of unknown origin in `texts/test/` and each of the four known texts in `texts/train/`. The author whose known text has the lowest distance to the unknown text will be assumed to be the true author. The distance can be computed based on either the POS frequencies, which in this case represent [syntactic](https://en.wikipedia.org/wiki/Syntax) features, or the noun synsets, which represent [semantic](https://en.wikipedia.org/wiki/Semantics) features. Both can vary from author to author and can contain clues as to the authorship.  

Write a function `find_closest_author(authors_pos_freqs, authors_noun_synsets, test_pos_freqs, test_noun_synsets, method="pos")` in `classification.py`. The argument `authors_pos_freqs` is a dictionary with known author names as keys and `pos_freqs` as values. The same structure holds for `authors_noun_synsets`. The arguments `test_pos_freqs` and `test_noun_synsets` are the `pos_freqs` and `synsets` of the unknown text whose authorship we will determine. The `method` keyword determines the distance type and can assume the value `pos` or `synsets`.  

For both methods, first compute the distance of the test text to the known texts based on the selected `method`, then return the author name as a `str` whose text has the lowest distance to the test text.  

For the `pos` method, use the Jensen-Shannon distance [`scipy.spatial.distance.jensenshannon`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.jensenshannon.html), since it is especially suited to probabilities.  

For the `synsets` method, use the Hamming distance [`scipy.spatial.distance.hamming`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.hamming.html), a set-based distance function. For that, you will first have to convert the two sets into boolean vectors that contain a boolean value for each element in the union of the two sets that tells whether or not the element is contained in the represented set.  

**Example:** The boolean representations of sets `a = {1, 2, 3}` and `b = {3, 5, 1}` would be `[True, True, True, False]` and `[True, False, True, True]`, with the implicit index being `[1, 2, 3, 5]`. So if the boolean value at index `0` is `True`, that means the element `1` is in the set. If the boolean value at index `1` is `True`, that means the element `2` is in the set. If the boolean value at index `2` is `True`, that means the element `3` is in the set, and if the boolean value at index `4` is `True`, that means the element `5` is in the set.  

**Note:** In a real-world appliatcion, one would of course use more sophisticated learning algorithms and more features (e.g. average sentence length, typical verbs, etc.) to identify the author. This is just of a toy example. 

> Good luck!
