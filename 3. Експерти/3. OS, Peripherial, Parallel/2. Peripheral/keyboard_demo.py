import turtle
import keyboard

turtle.speed('slow')

while True:
    if keyboard.is_pressed('q'):
        print("Thank you!")
        break

    if keyboard.is_pressed('w'):
        turtle.forward(1)
    if keyboard.is_pressed('a'):
        turtle.left(20)
    elif keyboard.is_pressed('d'):
        turtle.right(20)
