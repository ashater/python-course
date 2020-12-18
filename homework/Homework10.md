# Homework 10

We covered how to detect y and x coordinates for the ball. We also separated X and Y speed to the ball can go not only 90 degrees. 

Homework: Given ```move``` function below please add code to detect parts of the paddle collision and apply different Y speed to that.

 Please note you need to detect range of X axis because the paddle is split into three components. 


```python

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
    # if ball_x > pad_x and ball_x < pad_x + player_width:
    #     ballspeed_x = ballspeed_x * -1

    if first third of paddle hit:
        change speed
    if middle of paddle hit:
        change direction
    if last part of paddle hit:
        change direction/speed


```

