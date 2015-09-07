def name_tag(first_name, last_name):
    full_name = "My name is %s %s" % (first_name, last_name)
    return full_name

def test(first_name, last_name):
    print name_tag(first_name, last_name)
    
test("Joe", "Warren")
test("Scott", "Rixner")
test("John", "Greiner")