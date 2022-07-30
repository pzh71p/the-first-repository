import turtle
import time

t = turtle.Pen()
t.speed(0)
t.width(15)
t.pencolor("lemon chiffon")
turtle.bgcolor("darkblue")
turtle.tracer(False)

turtle.tracer(True)
turtle.onscreenclick(t.setpos)
turtle.done()
