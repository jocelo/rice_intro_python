import math

def circle_area(radius):
    pi = math.pi
    area = pi * (radius**2)
    return area

def test(radius):
    print "A circle with a radius of " + str(radius),
    print "inches has an area of",
    print str(circle_area(radius)) + " square inches."

test(8)
test(3)
test(12.9)