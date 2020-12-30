"""
Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase
"""

from string import punctuation, whitespace

book = 'word.txt'

with open(book, 'r') as fd:
    words = fd.read().split()

#remove punctuation, whitespace, uppercase
def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
print("{} has {} 'words'".format(book, len([clean(word) for word in words])))
