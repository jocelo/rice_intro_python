def future_value(present_value, annual_rate, years):
    future_value = present_value*( 1+(0.01*annual_rate))**years
    return future_value

def test(present_value, annual_rate, years):
    """Tests the future_value function."""
    
    print "The future value of $" + str(present_value) + " in " + str(years),
    print "years at an annual rate of " + str(annual_rate) + "% is",
    print "$" + str(future_value(present_value, annual_rate, years)) + "."

test(1000, 7, 10)
test(200, 4, 5)
test(1000, 3, 20)