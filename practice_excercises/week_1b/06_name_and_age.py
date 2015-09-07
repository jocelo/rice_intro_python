def name_and_age(name, age):
    returnString = ''
    if (age<0):
        returnString = 'Error: Invalid age'
    else:
        returnString = '%s is %s years old.' % (
        name,age)
    return returnString

def test(name, age):
    """Tests the name_and_age function."""
    
    print name_and_age(name, age)
    
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)