"""
    Write a function called is_abecedarian that returns True if the letters in a word
    appear in alphabetical order (double letters are ok). How many abecedarian words are there
        
"""

def is_abecedarian(word):
        for i in range(len(word)):
                for j in range(i+1, len(word)):
                        if ord(word[i]) > ord(word[j]):
                                return False
        return True
        
def count_abecedarian(word):
        ctr = 0
        for c in word:
            if is_abecedarian(c):
                ctr += 1
        print(ctr)

wordlist = open("./Exercise1.py")                
words = [line.strip() for line in wordlist]
count_abecedarian(words)
