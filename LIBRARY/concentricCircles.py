import turtle 
turtle = turtle.Turtle()
turtle.screen.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
while(True):
    for i in range(6):
        for colors in ["cyan", "blue", "magenta", "green", "red", "orange"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)

tutrle.hideturtle()
turtle.mainloop()