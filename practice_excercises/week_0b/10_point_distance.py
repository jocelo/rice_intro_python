#x0 = 2
#y0 = 2
#x1 = 5
#y1 = 6

#x0 = 1
#y0 = 1
#x1 = 2
#y1 = 2

x0 = 0
y0 = 0
x1 = 3
y1 = 4

distance = ( ((x0-x1)**2) + ((y0-y1)**2) ) ** (1.0/2.0)

print "The distance from (" + str(x0) + ", " + str(y0) + ") to",
print "(" + str(x1) + ", " + str(y1) + ") is " + str(distance) + "."