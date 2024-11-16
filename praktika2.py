import turtle
wn=turtle.Screen()
wn.setup(width=500, height=500)
blue=turtle.Turtle()
blue.speed(0)  
def curve():
    for i in range(250):
        blue.right(1)
        blue.forward(1)
def heart():
    blue.fillcolor('blue')
    blue.begin_fill()
    blue.left(250)
    blue.forward(200)
    curve()
    blue.left(150)
    curve()
    blue.forward(100)
    blue.end_fill()
heart()
blue.hideturtle()
turtle.done()