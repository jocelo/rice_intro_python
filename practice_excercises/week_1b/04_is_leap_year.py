# Compute whether the given year is a leap year.

###################################################
# Is leapyear formula
# Student should enter function on the next lines.

def is_leap_year(year):
    if int(year)%4 != 0:
        is_leap = False
    elif int(year)%100 != 0:
        is_leap = True
    elif int(year)%400 != 0:
        is_leap = False
    else:
        is_leap = True
    
    return is_leap

###################################################
# Tests
# Student should not change this code.

def test(year):
    """Tests the is_leapyear function."""
    if is_leap_year(year):
        print year, "is a leap year."
    else:
        print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2013)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
