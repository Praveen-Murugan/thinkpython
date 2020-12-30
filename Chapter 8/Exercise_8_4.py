"""
There is a string method called count that is similar to the function in the previous
exercise. Read the documentation of this method and write an invocation that counts the number of
as in 'banana'.
"""

word = "banana"
print(word.count("a"))


"""
Find and fix the second error in this function.

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)

    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True
"""
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1 
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True
print(is_reverse('hello','olleh'))

