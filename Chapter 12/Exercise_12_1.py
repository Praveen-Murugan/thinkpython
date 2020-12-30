"""
Many of the built-in functions use variable-length argument tuples. For example,
max and min can take any number of arguments:
Write a function called sumall that takes any number of arguments and returns their sum.


"""
def sumall(*args):
    return sum(args)
