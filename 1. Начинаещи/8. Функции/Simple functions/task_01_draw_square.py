# import turtle
#
side = 30
#
#
# def draw_square():      # draw square
#     for n in range(4):
#         turtle.forward(side)
#         turtle.left(90)
#
#
# draw_square()

import turtle
turtle.speed("slow")

def draw_square():
    for i in range (4):
        turtle.left(90)
        turtle.forward(side)
        turtle.done

draw_square()
