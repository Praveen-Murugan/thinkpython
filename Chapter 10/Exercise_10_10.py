"""
 Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?
Hint: use the time module to measure elapsed time

"""

import time

wordlist = open("./word.txt")

def make_word_list():
    new_wordlist = []
    for word in wordlist:
        word = word.strip()
        new_wordlist.append(word)
    return new_wordlist


def make_word_list2():
    new_wordlist = []
    for word in wordlist:
        word = word.strip()
        new_wordlist += [word]
    return new_wordlist
start_time = time.clock()
make_word_list()
end_time = time.clock()
print("Appending to make list time: " + str(end_time - start_time))

start_time = time.clock()
make_word_list2()
end_time = time.clock()
print("Concatenating to make list time: " + str(end_time - start_time))

