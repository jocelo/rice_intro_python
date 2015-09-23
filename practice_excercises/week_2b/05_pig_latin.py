import simplegui

def pig_latin(word):
    first_letter = word[0]
    rest_of_word = word[1 : ]
    result = ''

    if first_letter in ['a','e','i','o','u']:
        result = '%sway' % (word)
    else:
        result = '%s%say' % (rest_of_word,first_letter)
    print result

def get_input(word):
    pig_latin(word)

frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Insert the word for pig latin-ization", get_input , 200)

frame.start()

get_input("pig")
get_input("owl")
get_input("tree")
