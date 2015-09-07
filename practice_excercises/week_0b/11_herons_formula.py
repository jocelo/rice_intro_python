#x0, y0 = 0, 0
#x1, y1 = 3, 4
#x2, y2 = 1, 1

#x0, y0 = -2, 4
#x1, y1 = 1, 6
#x2, y2 = 2, 1

x0, y0 = 10, 0
x1, y1 = 0, 0
x2, y2 = 0, 10

a = ((x0-x1)**2+(y0-y1)**2) ** (1.0/2.0)
b = ((x1-x2)**2+(y1-y2)**2) ** (1.0/2.0)
c = ((x0-x2)**2+(y0-y2)**2) ** (1.0/2.0)

semi = (a+b+c)/2.0
area = (semi*(semi-a)*(semi-b)*(semi-c)) ** (1.0/2.0)

print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
print "(" + str(x1) + "," + str(y1) + "), and",
print "(" + str(x2) + "," + str(y2) + ") has an area of " + str(area) + "."