import turtle
t = turtle.Pen()
a = 1
b = 1
print(a, b)
t.hideturtle()

for i in range(10):
    a += b
    print(f"{a}\n")
    t.circle(a, -90)
    b += a
    print(f"{b}\n")
    t.circle(b, -90)
turtle.done()
