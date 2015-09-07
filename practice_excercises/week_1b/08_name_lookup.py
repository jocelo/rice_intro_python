def name_lookup(first_name):
    names = {'Joe':'Warren',
            'Scott':'Rixner',
            'John':'Greiner',
            'Stephen':'Wong'}
    if first_name in names:
        return names[first_name]
    else:
        return '#Error: Not an instructor'

def test(first_name):
    """Tests the name_lookup function."""
    
    print name_lookup(first_name)
    
test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")