def rectangle_perimeter(width, height):
    res = int(width)*2+int(height)*2
    return res

def test(width, height):
    print "A rectangle " + str(width) + " inches wide and " + str(height),
    print "inches high has a perimeter of",
    print str(rectangle_perimeter(width, height)) + " inches."

test(4, 7)
test(7, 4)
test(10, 10)