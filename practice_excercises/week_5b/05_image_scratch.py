import simplegui

img = simplegui.load_image("https://31.media.tumblr.com/avatar_bd0b76f98e4d_128.png")

# Handler to draw on canvas
def draw(canvas):
    if img.get_width() != 0:
        o_img_size = [img.get_width(),img.get_height()]
        o_img_pos = [o_img_size[0]/2,o_img_size[1]/2]
        canvas.draw_image(img, o_img_pos,o_img_size, [150,100],o_img_size)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Image draw from scratch", 300, 200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
