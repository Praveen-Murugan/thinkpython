"""
Write a function called do_n that takes a function object and a number, n, as arguments, and that calls the given function n times

"""
def do_n(function,number):
    for i in range(4):
        function()

def example_function():
    print("Function Called")

do_n(example_function,4)
