import random

def number_to_fortune(number):
    # Fill in your code here.
    # Use an if...elif...else statement
    # to check each of the numbers between 0 and 7
    # and return the fortune as a string.
    options = {
    0:"Yes, for sure!",
    1:"Probably yes.",
    2:"Seems like yes...",
    3:"Definitely not!",
    4:"Probably not.",
    5:"I really doubt it...",
    6:"Not sure, check back later!",
    7:"I really can't tell" }
    
    if number in options:
        result = options[number]
    else:
        result = "Error: Key not found"

    return result

def mystical_octosphere(question):
    answer_number = random.randrange(0,7)
    answer_fortune = number_to_fortune(answer_number)

    print 'Your question was...  %s' % question
    print 'You shake the mystical octosphere.'
    print 'The cloudy liquid swirls, and a reply comes into view...'
    print 'The mystical octosphere says... %s' % answer_fortune
    print

mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")