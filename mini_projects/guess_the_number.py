# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# globals
secret_number = 0
range = 100
lives = 0

# helper function to initialize lives
def generate_lives():
    global lives
    lives = int( math.ceil( math.log(range, 2) ) )

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number

    # init secret number
    secret_number = random.randrange(0,range)

    # reset lives
    generate_lives()

    # New Game messages
    print 'I have generated a new secret number.'
    print 'Within range [0,%s).' % range
    print 'So you have %s guesses to spend' % lives
    print 'Good luck!!' % secret_number

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global range
    range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global range
    range = 1000
    new_game()

def input_guess(guess):
    global lives

    # main game logic goes here
    guess_number = int(guess)
    print 'Your guess is %s' % guess_number

    # validate user guess against secret number
    if secret_number > guess_number:
        print 'Higher'
    elif secret_number < guess_number:
        print 'Lower'
    else:
        print 'Correct!!'
        print '------------------------------------'
        new_game()

    # check remaining lives
    lives -= 1
    if lives == 0:
        print ' !! GAME OVER !! You have used all the guesses...'
        print '(The secret number was: %s)' % secret_number
        print '------------------------------------'
        new_game()

    print ' > %s guesses remaining' % lives

# create frame
frame = simplegui.create_frame("Guess my number! v1.0", 300, 200)

# register event handlers for control elements and start frame
frame.add_input("Enter your guess and hit enter!", input_guess, 200)
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)

frame.start()

# call new_game
new_game()

# always remember to check your completed program against the grading rubric

