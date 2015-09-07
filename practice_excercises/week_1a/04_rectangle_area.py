def rectangle_area(width, height):
    area = int(width)*int(height)
    return area

def test(width, height):
    print "A rectangle " + str(width) + " inches wide and " + str(height),
    print "inches high has an area of",
    print str(rectangle_area(width, height)) + " square inches."

test(4, 7)
test(7, 4)
test(10, 10)