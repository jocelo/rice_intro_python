import simplegui

def set_red():
    global color
    color = "red"

def set_blue():
    global color
    color = "blue"

def print_color():
    print color

frame = simplegui.create_frame("Set and print colors", 200, 200)

frame.add_button("Print Color", print_color, 200)
frame.add_button("Set red", set_red, 200)
frame.add_button("Set blue", set_blue, 200)

frame.start()

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()
