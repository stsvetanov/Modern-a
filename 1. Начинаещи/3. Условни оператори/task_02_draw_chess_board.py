import turtle

side = 30

size = input("Enter chess board size: ")
size = int(size)


def draw_square():      # draw square
    for n in range(4):
        turtle.forward(side)
        turtle.left(90)


for k in range(size):
    for j in range(size):
        if (k + j) % 2 == 0:
            turtle.begin_fill()

        draw_square()

        turtle.end_fill()
        turtle.forward(side)

    turtle.penup()
    turtle.goto(0, side * (k + 1))
    turtle.pendown()

turtle.exitonclick()
