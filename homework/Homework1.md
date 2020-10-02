In our class on Thursdays we've covered a lot of concepts very quick:
- We've installed Python using [Anaconda Distribution](https://www.anaconda.com/products/individual)
- We'v learned how to use IPython console for quick REPL Python interaction
- We've looked at ```print``` command 
- We've looked at creating variables 
```python 
my_name = 'Ari'
print("My name is" + my_name)
Output: My name is Ari
```


- We've created a Python list of names
```python
my_names = ['Ari', 'Leo','Phillip','Avah']

for name in my_names:
    print("My name is "+name)

```
- We have learned how to use basic loops using ```range``` function:
```python
for i in range(0,100,1):
    print(i)
```

- We have learned Python package ```turtle```

- List of commands learned:
    - ```turtle.clearscreen()```
    - ```turtle.shape("turtle")```
    - ```turtle.forward()``` 
    - ```turtle.backward()```
    - ```turtle.left()```


- At the end we wrote our advanced set of loops with showing and moving our turtle around:

```python
# with just repeating same commands with out using i variable
for i in range(0,100,1):
   turtle.forward(100)
   turtle.left(100)

#  and moving turtle all around because value of variable i changing

for i in range(0,500,40):
   turtle.forward(100+i)
   turtle.left(100+i)
```

