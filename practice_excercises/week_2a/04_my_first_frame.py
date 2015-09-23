import simplegui

message = "My first frame!"

def click():
    print message

frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)

frame.start()
