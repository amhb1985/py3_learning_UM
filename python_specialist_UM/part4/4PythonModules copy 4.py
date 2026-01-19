#trying againg mit Turtule test

import turtle
wm = turtle.Screen()

elan = turtle.Turtle()

distance =  50
for _ in range(25):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 5

