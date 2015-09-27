# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# Event handlers for buttons
def start_handler():
    timer.start()

def stop_handler():
    timer.stop()

def reset_handler():
    global counter
    counter = 0
    stop_handler()

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)

frame.add_button('Start timer', start_handler, 150)
frame.add_button('Stop timer', stop_handler, 150)
frame.add_button('Restart timer', reset_handler, 150)

# Start timer
frame.start()
timer.start()

