from turtle import *

clearscreen()
screensize(500,500)
bob = Turtle()
bob.speed(8)

for i in range(1, 181):
    bob.forward(2)
    bob.right(2)

exitonclick()
