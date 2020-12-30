"""
Modify find so that it has a third parameter, the index in word where it should start looking.
"""

def find(word, letter, starting_index=0):
    index = starting_index
    while index < len(word):
        if word[index] == letter:
            return index
        index+=1
    return -1
print(find('banana','a',4))

"""
Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
"""

def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    print(count)
count('banana','a')

"""
Rewrite this function so that instead of traversing the string, it uses the three-parameter version of find from the previous section.
"""

def count_new(string, letter):
    count = 0
    starting_index = 0
    while starting_index < len(string):
        if find(string, letter, starting_index) == -1:
            print("None")
            break
        else:
            count += 1
            starting_index = find(string, letter, starting_index) + 1
    return count
print(count_new('banana','a'))
