# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.

import random

def powerball(ball):
    print "Today's numbers are %s, %s, %s, %s, and %s. The Powerball number is %s." %  (random.randrange(1,60),random.randrange(1,60),random.randrange(1,60),random.randrange(1,60),random.randrange(1,60),ball)
    
###################################################
# Tests
# Student should not change this code.
    
powerball(random.randrange(1,36))
powerball(random.randrange(1,36))
powerball(random.randrange(1,36))
