import turtle

iter = input("Enter # of iterations: ")
iter = int(iter)

angle = input("Enter angle: ")
angle = int(angle)

distance = input("Enter distance: ")
distance = int(distance)

count = 0

while count < iter:
    turtle.forward(distance)
    turtle.left(angle)
    count += 1

turtle.done()