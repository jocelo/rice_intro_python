import math

def circle_circumference(radius):
    pi = math.pi
    circum = 2 * pi * radius
    return circum

def test(radius):
    print "A circle with a radius of " + str(radius),
    print "inches has a circumference of",
    print str(circle_circumference(radius)) + " inches."

test(8)
test(3)
test(12.9)