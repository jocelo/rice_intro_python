# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui

total_ticks = 0
first_click = True
elapsed = 0

# Timer handler
def tick():
    global elapsed
    elapsed += 1

# Button handler
def click():
    global elapsed
    global first_click

    if first_click:
        timer.start()
    else:
        timer.stop()
        print 'time between clicks in 1/100 sec was %s' % elapsed
        elapsed = 0
    first_click = not first_click

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()

