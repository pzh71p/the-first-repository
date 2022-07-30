import turtle
import random
import time

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["lemon chiffon","gold","limegreen","skyblue","snow","tan","salmon"]
color_background = ["light pink","seashell","wheat","black","whitesmoke"]
choose = 0
heading = 90
width = 1
bgcolor = 0
bgcolor_choose = "black"
turtle.tracer(False)

t.pencolor(colors[choose])
t.width(1.5)
t.setheading(heading)

def left():
    t.left(30)
def right():
    t.right(30)
def down():
    global heading
    heading-=90
    t.setheading(heading)
    t.forward(10)
def up():
    t.forward(10)
def pencolor_choose():
    choose = random.randint(0,6)
    t.pencolor(colors[choose])
def nextbackground():
    global bgcolor_choose,bgcolor
    bgcolor = random.randint(0,4)
    bgcolor_choose = color_background[bgcolor]
    turtle.bgcolor(bgcolor_choose)

turtle.tracer(True)    
turtle.bgcolor(bgcolor_choose)
turtle.onkeypress(up,"Up")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.onkeypress(down,"Down")
turtle.onkeypress(pencolor_choose,"space")
turtle.onkeypress(nextbackground,"w")
turtle.listen()
turtle.done()