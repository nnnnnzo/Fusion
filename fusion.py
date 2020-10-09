
import turtle
def fusion (t, h, p):
    assert type(t) is turtle.Turtle
    assert type(p) is int and p >= 0
    
    t.forward(h)
    if p != 0:
        t.left(60)
        t.forward(h)
        t.right(180)
        t.forward(h)
        t.right(35)
        fusion(t,h,p-1)
def fusion2 (t, h, p):
    assert type(t) is turtle.Turtle
    assert type(p) is int and p >= 0
    
    t.forward(h)
    if p != 0:
        t.left(-95)
        t.forward(h)
        t.right(90)
        t.forward(h)
        t.right(200)
        fusion2(t,h,p-1)
    

t= turtle.Turtle()
t.goto(0,0)
t.setheading(90)
fusion(t,77,60) 
t.up()
t.goto(-90, 79)
t.down()
fusion2(t,50,80) 
