"""
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then print the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?

"""

fin = open("./Exercise1.py")

def avoids(word, string):
    for char in string:
        if char in word:
            return False
    return True

def calculate_avoiding_words():
    avoiding_count = 0
    avoid_string = input("What are the forbidden letters?")
    avoid_string = avoid_string.lower()

    for line in fin:
        word = line.strip()
        if avoids(word, avoid_string):
            avoiding_count += 1
    return avoiding_count
print(avoids("Apple", "abcd"))
print(calculate_avoiding_words())
