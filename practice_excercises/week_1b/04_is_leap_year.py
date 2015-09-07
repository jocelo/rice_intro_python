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