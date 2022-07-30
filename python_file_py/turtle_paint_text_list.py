import turtle
t = turtle.Pen()
t.speed(0)
t.penup()
turtle.bgcolor("black")

colors = ["red","yellow","blue","lemon chiffon","purple","orange","salmon","grey","pink","gold","yellowgreen","snow","tan","skyblue","limegreen"]
family = []
name = turtle.textinput("Family","Enter a name, or type [Enter] to end:")
while name !="":
    family.append(name)
    name = turtle.textinput("Family","Enter a name, or type [Enter] to end:")
for m in range(100):
    t.pencolor(colors[int(m%len(family))])
    t.penup()
    t.forward(m*4)
    t.pendown()
    t.write(family[m%len(family)],font=("Comic Sans MS",int((m+5)//5),"normal"))
    t.left(360/len(family)+2)
