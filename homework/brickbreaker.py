from turtle import Turtle, Screen

# game settings
ballspeed = 5
playerspeed = 20

cursor_size = 20
player_height = 20
player_width = 80

court_width = 1000
court_height = 600

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
    b.turtlesize(player_height / cursor_size, player_width / cursor_size)
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
    global ballspeed
    x, y = ball.position()
    pad_x, pad_y = paddle.position()

    # x = x + ballspeed
    # ball.setx(x)

    # here we check if we hit all the breaks
    if y > all_bricks[0].ycor() - player_height:
        ballspeed = ballspeed * -1

    # if you hit the position of the paddle reverse speed
    if y < pad_y + player_height + ballspeed:
        ballspeed = ballspeed * -1



    # if you are good, please add check for bounds
    y = y - ballspeed
    ball.sety(y)



    screen.ontimer(move, 20)



# We assign up and down arre the paddle
screen.onkey(left, "Left") # binds Left key to the function left()
screen.onkey(right, "Right") # bind Right key to the function right()
screen.onkey(up, "Up")

screen.listen() # start listeing to keys

move() # start loop by calling move function
screen.mainloop() # start drawing