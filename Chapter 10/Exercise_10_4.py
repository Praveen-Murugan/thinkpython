"""
Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3]

"""

def middle(num_list):
    return num_list[1:-1]
l = [1,2,3,4]
print(middle(l))
