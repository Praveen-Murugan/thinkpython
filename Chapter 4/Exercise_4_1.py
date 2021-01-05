"""
Exercise 4.1. Download the code in this chapter from http: // thinkpython. com/ code/
polygon. py .
1. Write appropriate docstrings for polygon, arc and circle.
2. Draw a stack diagram that shows the state of the program while executing circle(bob,
radius). You can do the arithmetic by hand or add print statements to the code.
3. The version of arc in Section 4.7 is not very accurate because the linear approximation of the
circle is always outside the true circle. As a result, the turtle ends up a few units away from
the correct destination. My solution shows a way to reduce the effect of this error. Read the
code and see if it makes sense to you. If you draw a diagram, you might see how it works.

"""

import math

try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *


def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    # draw a circle centered on the origin
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)

    wait_for_user()
