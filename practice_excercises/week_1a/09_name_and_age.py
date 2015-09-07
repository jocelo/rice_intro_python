def name_and_age(name, age):
    full_name = "%s is %s years old." % (name, age)
    return full_name

def test(name, age):
    print name_and_age(name, age)
    
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", 46)