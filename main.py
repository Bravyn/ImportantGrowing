import os
import string

def analyze_text(filename):
    # Check if the input file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File '{filename}' not found")

    # Read the input file and split it into words
    with open(filename, 'r') as f:
        text = f.read().lower()
    words = text.translate(str.maketrans('', '', string.punctuation)).split()

    # Count the frequency of each word using a dictionary
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Sort the words by frequency and return the result as a list of tuples
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

analyze_text("test.txt")