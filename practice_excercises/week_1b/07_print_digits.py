def print_digits(figure):
    if figure<0 or figure>=100:
        print "#Error: Input is not a two-digit number."
        return
    tens = figure // 10
    ones = figure % 10
    print "The tens digit is %s, and the ones digit is %s." % (tens, ones)
    
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)