# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
b = list(a)
b[0] = 0
print "element in 0 position [%s] " % a[0]

###################################################
# Explanation
# list makes a true copy of the array
# hence the values are not referenced
# they lives in a separated section of memory


