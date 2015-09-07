def is_even(number):
    return number%2 == 0

def test(number):
    """Tests the is_even function."""
    if is_even(number):
        print number, "is even."
    else:
        print number, "is odd."

test(8)
test(3)
test(12)