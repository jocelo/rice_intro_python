def is_cool(name):
    names = ['Joe', 'John','Stephen']
    return name in names

def test(name):
    """Tests the is_even function."""
    
    if is_cool(name):
        print name, "is cool."
    else:
        print name, "is not cool."

test("Joe")
test("John")
test("Stephen")
test("Scott")