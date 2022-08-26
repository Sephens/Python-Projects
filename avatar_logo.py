from turtle import *
speed(0)
bgcolor('black')
color('purple')
hideturtle()
n=1
p=True
while True:
    circle(n)
    if p:
        n=n-1

    else:
        n=n+1
    if n==0 or n==10:
        p=not p
    left(2)
    forward(2)