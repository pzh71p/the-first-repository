import turtle
t = turtle.Pen()
t.speed(0)
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("Numbr of sides","how many sides in your spiral(2-6)", 4, 2, 6))
colors = ["lemon chiffon","gold","limegreen","skyblue","snow","tan","salmon"]
for m in range(50):
    t.forward(m*4)
    position = t.position()
    heading = t.heading() 
    for n in range(sides):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.width(m//6.5)
        t.circle(m*0.66)
        t.right(360/sides - 2)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides+2)    
















































#www.8xiz.com天堂 http://www.zsrcn.com/
