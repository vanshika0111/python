import turtle
turtle = turtle.Turtle()
turtle.getscreen().bgcolor("cyan")
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
turtle.color("magenta")

turtle.speed(25)
def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
            turtle.end_fill()

star(turtle,360)
turtle.done()