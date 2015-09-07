def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    result = ''
    
    # Student should complete function on the next lines.
    if first_letter in ['a','e','i','o','u']:
        result = '%sway' % (word)
    else:
        result = '%s%say' % (rest_of_word,first_letter)
    return result

def test(word):
    """Tests the pig_latin function."""
    
    print pig_latin(word)
    
test("pig")
test("owl")
test("python")