import simplegui

def reset():
    global count
    count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def print_count():
    print count

frame = simplegui.create_frame("Counter Frame",100,200)

frame.add_button("Reset", reset, 150)
frame.add_button("Increment", increment, 150)
frame.add_button("Decrement", decrement, 150)
frame.add_button("Print", print_count, 150)

frame.start()

reset()
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()
