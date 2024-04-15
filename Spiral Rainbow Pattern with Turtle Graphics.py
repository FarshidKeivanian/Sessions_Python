import turtle
import colorsys

m = turtle.Screen()
m.bgcolor("black")
s = turtle.Turtle()
s.speed(0)
s.pensize(1.5)
n = 50
h = 90

for i in range(270):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1/n
    s.color(c)
    s.forward(i * 2)
    s.left(145)

turtle.done()
