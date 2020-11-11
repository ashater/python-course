### Class 6 was a review session of Homework 5 and review of ```functions```
--- 
We have corrected your homework and defined different shapes. Using loops inside the function was key to concise code. We have also reviewed input parameter or input variables. 

```python
def my_square(square_size):  # <-- square_size is am input parameter/variable
  for side in range(4):
    turtle.forward(60)  #< --- missing parameter
    turtle.left(90)

# correct version

def my_square(square_size):
  for side in range(4):
    turtle.forward(square_size) #< --- corrected parameter
    turtle.left(90)
```

### We have also reviewed how to define function and their ```return``` values:

```python
def fixed_number(x):
    return 100 + x #<  ---- return input x + 100
fixed_number(200)
Output: 300
```
More complex example:

```python
def fixed_number_1(x):
    return 100 + x
def fixed_number_2(x):
    return 500 + x

When you call these function separately:

In [12]: fixed_number_1(100)
Out[12]: 200

In [13]: fixed_number_2(100)
Out[13]: 600

In [14]: fixed_number_1(fixed_number_2(100)) # we call function sequentially 
Out[14]: 700
```

First we call inner function ```fixed_number_2``` with input 100, that returns 200, and subsequently we call ```fixed_number_1``` with input as an output of ```fixed_number_2`` of 200 and return 500 + 200 = 700

---

## Homework 6

Building on the - [Homework 5](Homework5.md), we will create functional version of that homework. 

Using your own functions of drawing shapes, please create your code as just calling functions for each part of the work flow:

1. Create code to ask for user input and draw shapes using functions you've define for shapes. **Please use loops in the shape drawing code**.

The code should look something like below: 


```python
# your shape drawing shapes
def ...
```
```python
# function to ask for shape
def ..
```
```python
# function to draw shapes based on input value
def ...
```
```python
# main code to call functions

input_shape = function_to_ask_for_shape()
# function to draw shape based on your
my_drawing_with_if_statement(input_shape)

```
