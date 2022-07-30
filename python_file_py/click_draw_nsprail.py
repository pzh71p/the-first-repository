import turtle
import random

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["lemon chiffon","gold","limegreen","skyblue","snow","tan","salmon"]
heading = t.heading()
turtle.tracer(False)

def draw(n,c,s):
    t.pencolor(c)
    for i in range(n):
        t.forward(i)
        t.left(360/s + 1.0)
        t.width(1.3)
def click_draw(x,y):
    n = random.randint(20,65)
    c = random.choice(colors)
    s = random.randint(3,6)
    t.penup()
    t.setpos(x,y)
    t.setheading(heading)
    t.pendown()
    draw(n,c,s)
    t.penup()
    t.setpos(-x,y)
    t.setheading(heading+90)
    t.pendown()
    draw(n,c,s)
    t.penup()
    t.setpos(x,-y)
    t.setheading(heading-90)
    t.pendown()
    draw(n,c,s)
    t.penup()
    t.setpos(-x,-y)
    t.setheading(heading+180)
    t.pendown()
    draw(n,c,s)

turtle.tracer(True)    
turtle.onscreenclick(click_draw)
turtle.done()



