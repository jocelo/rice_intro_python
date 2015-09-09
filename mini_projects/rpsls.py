# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

# function to retrieve rules
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
    if name in names:
        return names.index(name)
    else:
        print "ERROR: key is not in the list of elements"

def number_to_name(number):
    names = ('rock','Spock','paper','lizard','scissors')
    if number >= 0 and number < len(names):
        return names[number]
    else:
        print "Error: number out of bounds: %s",number

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    print "Player chooses: %s" % player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print "Computer chooses: %s" % comp_choice

    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number) % 5

    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print "Player and computer tie!"
    elif difference <= 2:
        print "%s so... Player wins!" % printRules(player_number, comp_number)
    elif difference <= 4:
        print "%s so... Computer wins!" % printRules(player_number, comp_number)
    else:
        print "Hey don't cheat !!"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
