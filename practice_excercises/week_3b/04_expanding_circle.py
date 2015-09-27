# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui

WIDTH = 200
HEIGHT = 200
radius = 1
sign = +1

# Timer handler
def timer_handler():
    global radius
    global sign
    radius += 1*(sign)
    print radius
    if (radius >= 100 or radius <= 1):
        sign = sign * -1

# Draw handler
def draw_handler(canvas):
    canvas.draw_circle((WIDTH/2, HEIGHT/2), radius, 1, 'Red')

# Create frame and timer
frame = simplegui.create_frame("Circle", WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100,timer_handler)

# Start timer
frame.start()
timer.start()
