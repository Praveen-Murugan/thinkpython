"""
. The “rank” of a word is its position in a list of words sorted by frequency: the most
common word has rank 1, the second most common has rank 2, etc.
Zipf’s law describes a relationship between the ranks and frequencies of words in natural languages
(http: // en. wikipedia. org/ wiki/ Zipf's_ law ). Specifically, it predicts that the frequency,
f , of the word with rank r is:
f = cr−s
where s and c are parameters that depend on the language and the text. If you take the logarithm of
both sides of this equation, you get:
log f = log c − slog r
So if you plot log f versus log r, you should get a straight line with slope −s and intercept log c.
Write a program that reads a text from a file, counts word frequencies, and prints one line for each
word, in descending order of frequency, with log f and log r. Use the graphing program of your
choice to plot the results and check whether they form a straight line. Can you estimate the value of
s?
Solution: http: // thinkpython. com/ code/ zipf. py . To make the plots, you might have to
install matplotlib (see http: // matplotlib. sourceforge. net/ ).

"""

import math


def make_word_histogram(a_file):
    text = []
    fin = open(a_file)
    for line in fin:
        word = line.strip().split()
        text += word

    histo = {}
    for word in text:
        histo[word] = histo.get(word, 0) + 1

    return histo


def sort_by_first_item(item):
    return item[0]


def make_sorted_tuples_list(a_histo):
    tuples = a_histo.items()

    reversed_tuples =[(v, k) for (k, v) in tuples]
    reversed_tuples = sorted(reversed_tuples, key=sort_by_first_item, reverse=True)

    return reversed_tuples


def print_freq_and_rank_logs(list_of_tuples):

    new_list = []
    for r, (freq, word) in enumerate(list_of_tuples, 1):
        new_list += [(freq, word, r)]

    list_with_logs = [(w, math.log(f), math.log(r)) for (f, w, r) in new_list]

    for item in list_with_logs:
        print item[0] + "/ log f: " + str(item[1]) + " / log r: " + str(item[2])


def main(a_file):
    text = make_word_histogram(a_file)
    sorted_tuples = make_sorted_tuples_list(text)
    results = print_freq_and_rank_logs(sorted_tuples)
    return results
