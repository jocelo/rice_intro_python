import simplegui

def get_input(msg):
    print '%s' % msg

frame = simplegui.create_frame("Echo input", 200, 200)

frame.add_input('Insert a value to echo it', get_input, 200)

frame.start()

get_input("First test input")
get_input("Second test input")
get_input("Third test input")
