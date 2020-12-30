"""
Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None

"""

def chop(list):
    del list[0]
    del list[-1]
l = [1,2,3,4]
print(chop(l))
