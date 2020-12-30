"""
. Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled.” Solution: http: //
thinkpython. com/ code/ interlock. py . Credit: This exercise is inspired by an example at
http: // puzzlers. org .
1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a
word, starting from the first, second or third?

"""

from bisect import bisect_left

def make_wordlist():
    wordlist = open("./word.txt")
    list = []
    for line in wordlist:
        word = line.strip()
        list += [word]
    return list

wordlist = make_wordlist()

def in_bisect(word_list, word):
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def is_interlocked(word, word_list):
    first_word = ''
    second_word = ''
    for letter in word[::2]:
        first_word += letter
    for letter in word[1::2]:
        second_word += letter
    if in_bisect(word_list, first_word) and in_bisect(word_list, second_word):
        return True
    return False

def find_interlocked(word_list):
    interlocked_pairs = []
    for word in word_list:
        if is_interlocked(word, word_list):
            interlocked_pairs += [word + ": " + word[::2] + "/" + word[1::2]]
    return interlocked_pairs

print(find_interlocked(wordlist))
