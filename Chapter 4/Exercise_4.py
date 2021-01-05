"""
1. Write a function called square that takes a parameter named t, which is a turtle. It
should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the
program again.
2. Add another parameter, named length, to square. Modify the body so length of the
sides is length, and then modify the function call to provide a second argument. Run
the program again. Test your program with a range of values for length.
3. The functions lt and rt make 90-degree turns by default, but you can provide a
second argument that specifies the number of degrees. For example, lt(bob, 45)
turns bob 45 degrees to the left.
Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees.
4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
that draws an approximate circle by invoking polygon with an appropriate length
and number of sides. Test your function with a range of values of r.

Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
Another hint: if bob is too slow for you, you can speed him up by changing
bob.delay, which is the time between moves, in seconds. bob.delay = 0.01 ought
to get him moving.
5. Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle.

"""

from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

#1

def square(t):
    for i in range(4):
        fd(t,100)
        lt(t)

square(bob)

#2

def square2(t,l):
    for i in range(4):
        fd(t,l)
        lt(t)

x = int(input("Enter Length : "))
square2(bob,x)

#3

def polygon(t,l,n):
    for i in range(n):
        fd(t,l)
        lt(t,360/n)

y = int(input("Enter Length : "))
z = int(input("Enter number of edges : "))
polygon(bob,y,z)

#4

def circle(t,r):
    cir = 2 * 3.14 * r
    n = int(cir/4)+1
    length = cir / n
    polygon(t,n,length)

circle(bob,100)

#5

def arc(t, r, angle):
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    lt(t, step_angle/2)
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)
    rt(t, step_angle/2)


arc(bob, 100, 180)


wait_for_user()
