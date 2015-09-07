def print_digits(number):
    tens = number // 10
    ones = number % 10
    print "The tens digit is %s, and the ones digit is %s." % (tens, ones)
    
print_digits(42)
print_digits(99)
print_digits(5)