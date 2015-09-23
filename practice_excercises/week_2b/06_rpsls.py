import simplegui
import random

def printRules(one, two):
    rules = {
    0: {
        1: 'Spock evaporates rock',
        2: 'paper covers rock',
        3: 'rock crushes lizard',
        4: 'rock crushes scissors'},
    1:{
        2: 'paper disproves Spock',
        3: 'lizard poisons Spock',
        4: 'Spock smashes scissors'},
    2:{
        3: 'lizard eats paper',
        4: 'scissors cuts paper'},
    3:{
        4: 'scissors decapitates lizard'}
    }

    if (one in rules and two in rules[one]):
        return rules[one][two]
    else:
        return rules[two][one]

def name_to_number(name):
    names = 'rock','Spock','paper','lizard','scissors'
    result = 0
    try:
        result = names.index(name)
        return result
    except:
        return -1

def number_to_name(number):
    names = ('rock','Spock','paper','lizard','scissors')
    if number >= 0 and number < len(names):
        return names[number]
    else:
        print "Error: number out of bounds: %s",number

def rpsls(player_choice):
    print
    print "Player chooses: %s" % player_choice
    player_number = name_to_number(player_choice)
    if player_number == -1:
        print 'Error: Bad input "%s" to rpsls' % player_choice
        return
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses: %s" % comp_choice
    difference = (player_number - comp_number) % 5

    if difference == 0:
        print "Player and computer tie!"
    elif difference <= 2:
        print "%s so... Player wins!" % printRules(player_number, comp_number)
    elif difference <= 4:
        print "%s so... Computer wins!" % printRules(player_number, comp_number)
    else:
        print "Hey don't cheat !!"

def get_guess(guess):
    rpsls(guess)

frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)

frame.start()

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")
