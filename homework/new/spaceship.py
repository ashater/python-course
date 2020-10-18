import turtle

screen = turtle.Screen()


# click the image icon in the top right of the code window to see
# which images are available in this trinket
image = r"C:\work\python-course\homework\rocketship.gif"

# add the shape first then set the turtle shape
screen.addshape(image)
turtle.shape()

screen.bgcolor("lightblue")

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

screen.listen()
# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


screen.mainloop()  # This will make sure the program continues to run 