
### Class 7 was an introduction to building a video game

Please read [chapter 8](PFK_Classes.pdf) on use of Python classes, they are important for our game programming.


We mostly went over building blocks for BrickBreaker. 
We are moving away from running code in ```Ipython``` console, please use Run "filename" in PyCharm

Link to source: [brickbreaker.py](brickbreaker.py)

--- 

Your homework is to make changes in the ```move``` function:

- Please try move the ball down vs. up
- Please try to identify the ball hitting a paddle (using ```pad_x``` and ```pad_y``` variables and ```if``` statement)
- Please reverse direction when your ball strikes the paddle, note reversing ball is just changing addition vs. subtraction

```python


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


for x in range(0, 300, 100):
    create_brick(x, 200)

# Player 1 Movement
def right():
    x = paddle.xcor() # get current position
    x = x + playerspeed # add playerspeed to current position
    paddle.setx(x) # set the new X position

def left():
    x = paddle.xcor()# get current position
    x = x - playerspeed # subtract playerspeed to current position
    paddle.setx(x)

def move():
    x, y = ball.position()
    pad_x, pad_y = paddle.position()

    # x = x + ballspeed
    # ball.setx(x)

    #if you hit the position of the paddle reverse speed


    # if you are good, please add check for bounds
    y = y + ballspeed
    ball.sety(y)


    screen.ontimer(move, 20)



# We assign up and down arrow to move the paddle
screen.onkey(left, "Left") # binds Left key to the function left()
screen.onkey(right, "Right") # bind Right key to the function right()


screen.listen() # start listeing to keys

move() # start loop by calling move function
screen.mainloop() # start drawing
```

---


