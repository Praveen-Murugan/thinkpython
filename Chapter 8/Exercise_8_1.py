"""Write a function that takes a string as an argument and displays the letters backward,
one per line"""


def revStr(fruit):
    index = len(fruit) - 1
    while(index >= 0):
        print(fruit[index])
        index-=1
fruit = 'banana'
revStr(fruit)
print(fruit[::-1])

