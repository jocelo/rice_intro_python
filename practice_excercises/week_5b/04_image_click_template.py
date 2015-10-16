# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
IMG_SIZE = (95, 93)
IMG_ORG_POS = [IMG_SIZE[0]/2,IMG_SIZE[1]/2]
img_pos = [WIDTH/2, HEIGHT/2]

# load test image
img = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")
print img
# mouseclick handler
def click(pos):
    global img_pos
    img_pos = pos

# draw handler
def draw(canvas):
    canvas.draw_image(img,IMG_ORG_POS,IMG_SIZE,img_pos,IMG_SIZE)

# create frame and register draw handler
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()


