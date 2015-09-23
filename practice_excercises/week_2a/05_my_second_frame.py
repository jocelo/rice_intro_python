import simplegui

message = "My second frame!"

def click():
    print message

frame = simplegui.create_frame("My Second Frame", 200, 100)

frame.add_button("Click me", click)

frame.start()
