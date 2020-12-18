from turtle import Turtle, Screen

# game settings

ballspeed_x = 2
ballspeed_y = 2
playerspeed = 20

cursor_size = 20

# paddle settings
player_height = 20
player_width = 80

# court settings
court_width = 1000
court_height = 600

# brick settings
brick_height = 20
brick_width = 80



# Ball setup
ball = Turtle("circle")
ball.color("black")
ball.penup()
ball.speed("fastest")
ball.setx(0)


# paddle setup
paddle = Turtle("square")
paddle.turtlesize(player_height / cursor_size, player_width / cursor_size)
paddle.color("white")
paddle.penup()
paddle.sety(-300)
paddle.speed("fastest")


# screen setup
screen = Screen()
screen.title("Brickbreaker")
screen.bgcolor("grey")
screen.setup(width=1.0, height=1.0)


def create_brick(x, y):
    # paddle setup
    b = Turtle("square")
    b.turtlesize(brick_height / cursor_size, brick_width / cursor_size)
    b.color("white")
    b.penup()
    b.sety(y)
    b.setx(x)
    return b

all_bricks = [] # list
for x in range(0, 300, 100):
    all_bricks.append(create_brick(x, 200))

# Player 1 Movement
def right():
    x = paddle.xcor() # get current position
    x = x + playerspeed # add playerspeed to current position
    paddle.setx(x) # set the new X position

def left():
    global  ballspeed
    x = paddle.xcor()# get current position
    x = x - playerspeed # subtract playerspeed to current position
    paddle.setx(x)

def up():
    y = paddle.ycor() #gets Y location of the paddle
    y = y + playerspeed # add player speed to y variable
    paddle.sety(y) # set y coordinate of the paddle

def move():
    global ballspeed_x, ballspeed_y
    ball_x, ball_y = ball.position()
    pad_x, pad_y = paddle.position()


    # here we check if we hit all the breaks
    for current_brick in all_bricks:
        cur_brick_x, cur_brick_y = current_brick.position()
        cur_brick_x_start = cur_brick_x
        cur_brick_x_end = cur_brick_x + brick_width

        if ball_y > (cur_brick_y - player_height + ballspeed_y) and (ball_x > cur_brick_x_start and ball_x < cur_brick_x_end):
            ballspeed_x = ballspeed_x * -1
            ballspeed_y = ballspeed_y * -1

    # if you hit the position of the paddle reverse speed
    if ball_y < (pad_y + player_height + ballspeed_y):
        ballspeed_y = ballspeed_y * -1.0

    # please create 3 if statements, depending on where you hit on the paddle, you change the speed
    if ball_x > pad_x and ball_x < pad_x + player_width:
        ballspeed_x = ballspeed_x * -1






    # if you are good, please add check for bounds
    ball_y = ball_y - ballspeed_x
    ball.sety(ball_y)
    ball_x = ball_x - ballspeed_y
    ball.setx(ball_x)

    screen.ontimer(move, 20)



# We assign up and down arre the paddle
screen.onkey(left, "Left") # binds Left key to the function left()
screen.onkey(right, "Right") # bind Right key to the function right()
screen.onkey(up, "Up")

screen.listen() # start listeing to keys

move() # start loop by calling move function
screen.mainloop() # start drawing