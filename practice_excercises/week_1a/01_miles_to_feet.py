def miles_to_feet(miles):
    feets = miles * 5280
    return feets

def test(miles):
    print str(miles) + " miles equals",
    print str(miles_to_feet(miles)) + " feet."

test(13)
test(57)
test(82.67)