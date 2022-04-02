import turtle

turtle.speed('slow')

number_of_iteration = input("Въведете брой итерации: ")
print(type(number_of_iteration))

number_of_iteration = int(number_of_iteration)

while number_of_iteration < 4:
    turtle.left(90)
    turtle.forward(250)
    number_of_iteration += 1

turtle.done()
