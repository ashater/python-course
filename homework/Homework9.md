# Homework 9 

We covered how to detect y and x coordinates for the ball. We tried to make sure when the ball go sideways, we can detect hitting the paddle and all bricks. Remember we need a for loop to detect collision of all the bricks. 

Homework: Given ```move``` function below please add code to detect X axis collision. Please note you need to detect range of X axis because the paddle and bricks are length of ```brick_width```


```python

    # here we check if we hit all the breaks
    for current_brick in all_bricks:
        cur_brick_x, cur_brick_y = current_brick.position()
        cur_brick_x_start = cur_brick_x
        cur_brick_x_end = cur_brick_x + brick_width

    if ball_y > cur_brick_y - player_height + ballspeed and  <YOUR CODE FOR X COLLISION DETECTION>:
        ballspeed = ballspeed * -1

    # if you hit the position of the paddle reverse speed
    if ball_y < (pad_y + player_height + ballspeed) and <YOUR CODE FOR X COLLISION DETECTION>:
        ballspeed = ballspeed * -1


```

