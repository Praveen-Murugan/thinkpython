"""
More anagrams!
1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.
Here is an example of what the output might look like:
[‘deltas’, ‘desalt’, ‘lasted’, ‘salted’, ‘slated’, ‘staled’]
[‘retainers’, ‘ternaries’]
[‘generating’, ‘greatening’]
[‘resmelts’, ‘smelters’, ‘termless’]
Hint: you might want to build a dictionary that maps from a set of letters to a list of words that can be spelled with those letters.
The question is, how can you represent the set of letters in a way that can be used as a key?

"""

def make_wordlist(file):
    result = []
    wordlist = open(file)
    for line in wordlist:
        word = line.strip()
        result += [word]
    return result

wordlist = make_wordlist("words.txt")

def find_anagrams(list_words):
    d = {}
    for item in list_words:
        letters = []
        for letter in item:
            letters += letter
        r = tuple(sorted(letters))
        if r in d:
            d[r].append(item)
        else:
            d[r] = [item]

    anagrams = []
    for item in d.values():
        if len(item) > 1:
            anagrams += [item]
    return anagrams

def find_anagrams2(list_words):
    d = {}
    for item in list_words:
        letters = []
        for letter in item:
            letters += letter
        r = tuple(sorted(letters))
        if r in d:
            d[r].append(item)
        else:
            d[r] = [item]

    anagrams = []
    for item in d.values():
        if len(item) > 1:
            anagrams += [item]

    sorted_anagrams = sorted(anagrams, key=len, reverse=True)
    return sorted_anagrams
