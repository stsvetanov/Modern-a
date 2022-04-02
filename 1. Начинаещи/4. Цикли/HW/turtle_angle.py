import turtle

count_angle = int(input("Въведете броят на ъглите: "))
size = round(200 / count_angle * 2)

if count_angle > 2:
    angle = 360 / count_angle
    for i in range(count_angle):
        turtle.left(angle)
        turtle.forward(size)
    turtle.done()
