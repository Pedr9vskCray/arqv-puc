from turtle import *

def draw(n: int):
    angle = 360/n

    clearscreen()
    screensize(500,500)
    bob = Turtle()
    bob.speed(2)

    for side in range(1, n+1):
        bob.forward(50)
        bob.right(angle)

n = int(input("Digite o número de lados do polígono que você deseja desenhar: "))

draw(n)

exitonclick()