import numpy as np
import spacy


def main():
    
    pos_freqs = get_pos_freqs("texts/train/alice_in_wonderland.txt")

    print("These are the calculated POS frequencies for 'Alice in Wonderland' by Lewis Carroll:")
    print(pos_freqs)
    print("Normalized frequencies should sum up to 1.00. The calculated POS frequencies sum up to: {:.2f}".format(pos_freqs.sum()))


def get_pos_freqs(filepath):
    """ 
    Function that returns an array containing the normalized frequencies of POS tags in a text.
    
    params:
    filepath -- The path to the text file
    """
    
    # load in the text file
    with open(filepath) as infile:
        content = infile.read()
    
    # create doc with spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(content)
    
    # count pos tags
    tags = list(spacy.parts_of_speech.IDS.keys())
    pos_freq = np.zeros(len(tags))
    
    for token in doc:
        idx = 0
        for tag in tags:
            if token.pos_ == tag:
                pos_freq[idx] += 1
                break # after the element is found, stop iteration
            idx += 1
            
    # normalize counts to give a probability distribution
    pos_freq_normalized = pos_freq / len(doc)

    # return normalized POS frequencies
    return pos_freq_normalized


if __name__ == "__main__":
    main()
