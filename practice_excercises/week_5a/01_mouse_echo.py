# Echo mouse click in console
import simplegui

###################################################
# Student should enter code below
cl = True

def mouse_handler(position):
    global cl
    if cl:
        print "click! at ", position
    else:
        print "and clack around ",position
    cl = not cl

frame = simplegui.create_frame('Mouse clicking', 100, 100)
frame.set_mouseclick_handler(mouse_handler)
frame.start()

###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)
