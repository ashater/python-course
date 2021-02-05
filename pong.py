from turtle import Turtle, Screen

# game settings
ballspeed = 3
playerspeed = 20

cursor_size = 20
player_height = 80
player_width = 20

true_paddle_height = 50
true_paddle_width = 20

border_height = 600
border_width = 600
court_width = 1000
court_height = 600

# Ball setup
ball = Turtle("circle")
ball.color("white")
ball.penup()
ball.speed("fastest")
ball.setx(0)

# screen setup
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)

# paddle setup
paddle = Turtle("square")
paddle.turtlesize(player_height / cursor_size, player_width / cursor_size)
paddle.color("blue")
paddle.penup()
paddle.setx(-300)
paddle.speed("fastest")

# paddle2 setup
paddle2 = Turtle("square")
paddle2.turtlesize(player_height / cursor_size, player_width / cursor_size)
paddle2.color("red")
paddle2.penup()
paddle2.setx(300)
paddle2.speed("fastest")

def up():
    y = paddle.ycor()  # get current position
    y = y + playerspeed  # add playerspeed to current position
    paddle.sety(y)  # set the new x position


def down():
    y = paddle.ycor()  # get current position
    y = y - playerspeed  # subtract playerspeed to current position
    paddle.sety(y)





def up2():
    y2 = paddle2.ycor()  # get current position
    y2 = y2 + playerspeed  # add playerspeed to current position
    paddle2.sety(y2)  # set the new x position


def down2():
    y2 = paddle2.ycor()  # get current position
    y2 = y2 - playerspeed  # subtract playerspeed to current position
    paddle2.sety(y2)




def border():
    # paddle setup
    border = Turtle("square")
    border.turtlesize(border_height / cursor_size, border_width / cursor_size)
    border.color("white")
    border.penup()
    border.sety(-300)
    border.speed("fastest")

def border2():
    # paddle setup
    border2 = Turtle("square")
    border2.turtlesize(border_height / cursor_size, border_width / cursor_size)
    border2.color("white")
    border2.penup()
    border2.sety(300)
    border2.speed("fastest")

def move():
    global ballspeed
    x, y = ball.position()
    pad_x, pad_y = paddle.position()
    pad2_x, pad2_y = paddle2.position()
    x = x + ballspeed
    ball.setx(x)
    # if you are good, please add check for bounds
    y = y + ballspeed
    ball.sety(y)
    #ball.write("%i,%i" % (x,y))

    #left side
    if y > pad_y - true_paddle_height and y < pad_y + true_paddle_height and x <= pad_x + true_paddle_width:
        ballspeed = ballspeed * -1

    #right side
    if y > pad2_y - true_paddle_height and y < pad2_y + true_paddle_height and x >= pad2_x - true_paddle_width:
        ballspeed = ballspeed * -1


    screen.ontimer(move, 20)


def score():
    pad_x, pad_y = paddle.position()
    pad2_x, pad2_y = paddle2.position()
    x, y = ball.position()
    s1=0
    s2=0
    if y < pad_y:
        s1 + 1
    if y < pad2_y:
        s2 + 1
    if s1 == 9:
        screen.write("BLUE WINS!!! AND IS A TRUE GAMER")
    if s2 == 9:
        screen.write("RED WINS!!! AND IS A TRUE GAMER")





# if you hit the position of the paddle reverse speed

border()


# We assign up and down are the paddle
screen.onkey(up, "q")  # binds q key to the function up for blue()
screen.onkey(down, "a")# binds a key to the function down for blue()
screen.onkey(up2, "p")# binds p key to the function up for red()
screen.onkey(down2, "l")# binds l key to the function down for red()

screen.listen()


move()
score()
screen.mainloop()  # start drawing
