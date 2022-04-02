# Да се начертае крадрат по зададена страна

import turtle

size = int(input("Enter size: "))
angle = 90
number_of_iterations = 10

for i in range(4):
    turtle.forward(size)
    turtle.left(angle)


turtle.done()


