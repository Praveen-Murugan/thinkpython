"""
Exercise 11
The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).
"""


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

#The above function returns true or false based on whether only the first letter is lowercase.



def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#The above function will always return “True” because it just checks if “c” is lowercase.



def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

#The above function returns true or false depending on whether the last letter in the string is lowercase.



def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#The above function works properly to check if any lowercase letters are present. As soon as one is discovered, flag changes to “True” and remains that way.



def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

#The above function tests to see if there are any uppercase letters, and if so returns false.
