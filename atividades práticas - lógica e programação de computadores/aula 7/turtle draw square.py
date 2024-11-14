from turtle import *

clearscreen()
screensize(500,500)
bob = Turtle()
bob.speed(2)

for side in range(4):
    bob.forward(100)
    bob.right(90)
    
exitonclick()