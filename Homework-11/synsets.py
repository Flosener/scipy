from nltk.corpus import wordnet

import numpy as np

import spacy
import nltk


def main():

    noun_synsets = get_noun_synsets("texts/train/alice_in_wonderland.txt")

    print("These are the calculated noun synsets for 'Alice in Wonderland' by Lewis Carroll:")
    print(noun_synsets)


def get_noun_synsets(filepath):

    """ 
    Function that returns a set of all WordNet synset names associated with the ten most frequent nouns in a text.
    
    params:
    filepath -- The path to the text file
    """
    
    # load in the text file
    with open(filepath) as infile:
        content = infile.read()
    
    # create doc with spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(content)
    
    # get all noun lemmas and respective counts
    lemma_dict = {}
    for token in doc:
        if token.pos_ == 'NOUN':
            if token.lemma_ not in lemma_dict:
                lemma_dict.update({token.lemma_ : 1})
            else:
                lemma_dict[token.lemma_] += 1
    
    # sort dictionary with lambda operator and get top 10 lemmas
    lemma_list_sorted = sorted(lemma_dict.items(), key=lambda item: item[1])
    top_ten = []
    for lemma in lemma_list_sorted[-10:]:
        top_ten.append(lemma[0])
        
    # get all synsets and add to set of synset names
    synsets = set()
    for lemma in top_ten:
        lemma_synsets = wordnet.synsets(lemma, pos="n")
        for synset in lemma_synsets:
            synsets.add(synset.name())

    # return the resulting set of synset names
    return synsets
    

if __name__ == "__main__":
    main()
