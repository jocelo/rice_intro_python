# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 10
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
runGame = True
winner = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    hor_vel = round( random.randrange(120, 240) / 60.0, 2)
    vert_vel = round( random.randrange(60, 180) / 60.0, 2)
    ball_pos = [WIDTH/2, HEIGHT/2]

    # ball's initial speed
    ball_vel = [hor_vel, vert_vel]

    # which player will "serve"
    ball_vel[0] *= 1 if direction else -1

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global runGame

    runGame = True

    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT/2]

    paddle1_vel = 0
    paddle2_vel = 0

    score1 = 0
    score2 = 0

    winner = 0

    # Randomly choose ball orientation
    if random.randrange(0,100) > 50:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, runGame, winner

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "Green")
    #canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    #canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] -= ball_vel[1]

    # draw ball
    # canvas.draw_circle(ball_pos, BALL_RADIUS, 12, 'Green', 'Green')
    canvas.draw_polygon([[ball_pos[0]-BALL_RADIUS, ball_pos[1]-BALL_RADIUS],
                        [ball_pos[0]+BALL_RADIUS, ball_pos[1]-BALL_RADIUS],
                        [ball_pos[0]+BALL_RADIUS, ball_pos[1]+BALL_RADIUS],
                        [ball_pos[0]-BALL_RADIUS, ball_pos[1]+BALL_RADIUS]], 12, 'Green', 'Green')

    # update paddle's vertical position, keep paddle on the screen
     # left player
    if paddle1_pos[1]-HALF_PAD_HEIGHT < 0:
        paddle1_pos[1] = HALF_PAD_HEIGHT

    if paddle1_pos[1]+HALF_PAD_HEIGHT > HEIGHT:
        paddle1_pos[1] = HEIGHT-HALF_PAD_HEIGHT

    paddle1_pos[1] += paddle1_vel

     # right player
    if paddle2_pos[1]-HALF_PAD_HEIGHT < 0:
        paddle2_pos[1] = HALF_PAD_HEIGHT

    if paddle2_pos[1]+HALF_PAD_HEIGHT > HEIGHT:
        paddle2_pos[1] = HEIGHT-HALF_PAD_HEIGHT

    paddle2_pos[1] += paddle2_vel

    # draw paddles
    # left player
    canvas.draw_line([paddle1_pos[0],paddle1_pos[1]-HALF_PAD_HEIGHT],
                     [paddle1_pos[0],paddle1_pos[1]+HALF_PAD_HEIGHT], PAD_WIDTH, "Green")

    canvas.draw_line([paddle2_pos[0],paddle2_pos[1]-HALF_PAD_HEIGHT],
                     [paddle2_pos[0],paddle2_pos[1]+HALF_PAD_HEIGHT], PAD_WIDTH, "Green")


    # determine whether paddle and ball collide
    # horizontal gutter collision
    if (ball_pos[1]-BALL_RADIUS <= 0) or (ball_pos[1]+BALL_RADIUS >= HEIGHT):
        ball_vel[1] *= -1

    if not runGame:
        canvas.draw_text(("Player "+winner+" won!"), (WIDTH/2-170, HEIGHT/2), 64, 'Green')
        return

    # vertical wall collision
    if (ball_pos[0]-BALL_RADIUS <= PAD_WIDTH):
        if int(ball_pos[1]) > paddle1_pos[1]-HALF_PAD_HEIGHT and int(ball_pos[1]) < paddle1_pos[1]+HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
        else:
            score2+=1
            spawn_ball(RIGHT)

    if (ball_pos[0]+BALL_RADIUS >= WIDTH-PAD_WIDTH):
        if int(ball_pos[1]) > paddle2_pos[1]-HALF_PAD_HEIGHT and int(ball_pos[1]) < paddle2_pos[1]+HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.2
        else:
            score1+=1
            spawn_ball(LEFT)

    # draw scores
    canvas.draw_text(str(score1), (WIDTH/2-110, 60), 64, 'Green')
    canvas.draw_text(str(score2), (WIDTH/2+60, 60), 64, 'Green')

    if score1 == 9 or score2 == 9:
        winner = '1' if score1 > score2 else '2'
        runGame = False

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 3
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -3
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 3

def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Reset Game",new_game,100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()

